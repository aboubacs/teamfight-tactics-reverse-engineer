from collections import deque
import utils
import uuid
import pygame
import random

from .shield_manager import ShieldManager
from .modifier import Modifier
from synergies import Assassin
from synergies import Cavalier
from synergies import Hellion

UNIT_IMAGE_WIDTH = 60

MOVE_TIME = 0.5
MOVE_TIME_ASSASSIN = 0.6

star_image = pygame.image.load('./images/star.png')
star_image = pygame.transform.smoothscale(star_image, (20, 20))
font = pygame.font.SysFont('Comic Sans MS', 12)

class UnitState:
    ATTACKING = 1
    MOVING = 2
    STUNNED = 3

class Unit:
    def __init__(self, cost, health, starting_mana, total_mana, attack_speed, attack_damage,
                 armor, magic_resist, attack_range, image_name, row, col, team, star_level, items=None, synergies=None,
                 forgotten_stacks=0, scale_hp_with_star_level=True, scale_ad_with_star_level=True):
        self._init_cost = cost
        self._init_health = health
        self._init_starting_mana = starting_mana
        self._init_total_mana = total_mana
        self._init_attack_speed = attack_speed
        self._init_attack_damage = attack_damage
        self._init_armor = armor
        self._init_magic_resist = magic_resist
        self._init_attack_range = attack_range
        self._init_team = team
        self._init_star_level = star_level
        self._init_items = items

        self.forgotten_stacks = forgotten_stacks
        self._all_modifiers = []
        self.uuid = uuid.uuid4()
        self.cost = cost
        self.star_level = star_level
        self.health = health
        if scale_hp_with_star_level:
            for _ in range(star_level-1):
                self.health *= 1.8
            if star_level == 0:
                self.health /= 1.8
        self.total_health = self.health
        self.mana = starting_mana
        self.total_mana = total_mana
        self.percent_mana_increase = 0
        self.base_attack_speed = attack_speed
        self.base_attack_speed_bonus_ratio_modifiers = Modifier(self)
        self.base_attack_damage = attack_damage
        self.flat_bonus_attack_damage_modifiers = Modifier(self)
        self.attack_damage_multiplier_modifiers = Modifier(self)
        if scale_ad_with_star_level:
            for _ in range(star_level-1):
                self.base_attack_damage *= 1.8
            if star_level == 0:
                self.base_attack_damage /= 1.8
        self.base_armor = armor
        self.flat_bonus_armor_modifiers = Modifier(self)
        self.base_magic_resist = magic_resist
        self.flat_bonus_magic_resist_modifiers = Modifier(self)
        self.attack_range = attack_range
        self.percent_damage_reduction_modifiers = Modifier(self)
        self.multitarget_percent_damage_reduction_modifiers = Modifier(self)
        self.armor_shred_percentage_modifiers = Modifier(self)
        self.magic_resist_shred_percentage_modifiers = Modifier(self)

        self.image_name = image_name
        self.image = pygame.image.load('./images/' + self.image_name + '.png')
        try:
            self.image = pygame.transform.smoothscale(self.image, (60, 60))
        except Exception:
            self.image = pygame.transform.scale(self.image, (60, 60))

        self.last_attacked_at = 0
        self.current_target = None
        self.spell_power = 100
        self.flat_bonus_spell_power_modifiers = Modifier(self)
        self.base_critical_chance = 0.25
        self.flat_bonus_crit_damage = 0
        self.spellweaver_ap_gain_per_cast = 0
        self.spellweaver_stacks = 0
        self.aa_count = 0
        self.cannoneer_active = False
        self.cannoneer_ad_ratio = 0
        self.has_revenant = False
        self.bonus_dodge = 0
        self.legionnaire_omnivamp_ratio = 0

        self.stacks = {}
        self.dots = []
        self.on_hit_effects = []

        self.row = row
        self.col = col
        self.team = team
        self.star_level = star_level

        self.is_moving = False
        self.has_moved = False
        self.moves_until = None

        self.has_spell_shield = False
        self.remove_spellshield_at_next_tick = False

        self.next_cast_spell_at = None
        self.cast_time = 0.01

        self.stunned_until = -1
        self.is_stunned = False

        self.hemoragy_until = -1
        self.has_hemoragy = None

        self.is_targetable = True
        self.untargetable_until = -1

        self.is_under_revive = False
        self.under_revive_until = -1
        self.revive_with = 0

        self.mana_lock_time = 1.00
        self.mana_locked_until = -50
        self.is_mana_locked = False

        # NOTE: only for slows
        self.attack_speed_multiplier_modifiers = Modifier(self)  # TODO: currently multiplicative (might be additive of even max)
        self.flat_damage_reduction_modifiers = Modifier(self)

        self.is_dead = False

        self.items = items or []
        self.synergies = synergies or []
        self.shield_manager = ShieldManager()

        self.mana_per_auto = 10
        self.innate_bonus_damage_multiplier_modifiers = Modifier(self)
        self.additional_percent_damage_reduction = 0

        self.has_had_target = False
        self.is_hellion_spawn = False
        self.should_spawn_hellion = False

        self.is_under_zephyr = False
        self.under_zephyr_until = -1

        self._TIME = 0

    def to_log_json(self):
        return {
            'name': self.image_name,
            'health': self.health,
            'total_health': self.total_health,
            'row': self.row,
            'col': self.col,
            'star_level': self.star_level,
            'team': self.team,
            'mana': self.mana,
            'total_mana': self.total_mana,
            'percent_mana_increase': self.percent_mana_increase,
            'shield': self.shield_manager.get_total_shield_value(),
            'is_stunned': self.is_stunned,
            'is_under_zephyr': self.is_under_zephyr,
            'is_under_revive': self.is_under_revive,
            'has_hemoragy': self.has_hemoragy,
            'attack_damage': self.get_attack_damage(),
            'attack_speed': self.get_attack_speed(),
            'spell_power': self.get_spell_power(),
            'magic_resist': self.get_magic_resist(),
            'armor': self.get_armor(),
            'items': [item.image_name for item in self.items]
        }

    def enemies(self, board):
        return [u for u in board.units if u.team != self.team]

    def targetable_enemies(self, board):
        return [u for u in self.enemies(board) if u.is_targetable]

    def allies(self, board):
        return [u for u in board.units if u.team == self.team]

    def targetable_allies(self, board):
        return [u for u in self.allies(board) if u.is_targetable]

    def add_shield_effect(self, shield_value, shield_duration, identifier=""):
        self.shield_manager.add_shield_effect(self._TIME, shield_value, shield_duration, identifier)

    def trigger_items_add(self, board):
        for item in self.items:
            item.trigger_on_add(board, self)

    # hack but fast
    def get_olaf_bonus_as(self):
        return 0

    def get_attack_speed(self):
        bonus_as = self.base_attack_speed_bonus_ratio_modifiers.sum()
        bonus_as += self.get_olaf_bonus_as()
        for item in self.items:
            bonus_as += item.get_attack_speed_bonus()
        attack_speed = self.base_attack_speed * (1 + bonus_as)
        attack_speed *= self.attack_speed_multiplier_modifiers.min() or 1  # We are affected by the slowest slow (all ratios are < 1)
        return attack_speed

    def get_cricical_damage(self):
        base_damage = 1.5
        base_damage += self.flat_bonus_crit_damage
        for item in self.items:
            base_damage += item.get_critical_damage_bonus(self)
        return base_damage

    def get_spell_power(self):
        spell_power = self.spell_power
        spell_power += self.flat_bonus_spell_power_modifiers.sum()
        for item in self.items:
            spell_power += item.get_spell_power_bonus()
        return spell_power

    def get_attack_damage(self):
        bonus_ad = self.flat_bonus_attack_damage_modifiers.sum()
        for item in self.items:
            bonus_ad += item.get_attack_damage_bonus()
        return (self.base_attack_damage + bonus_ad) * (1 + self.attack_damage_multiplier_modifiers.sum())

    def get_armor(self):
        bonus_armor = self.flat_bonus_armor_modifiers.sum()
        for item in self.items:
            bonus_armor += item.get_armor_bonus()
        armor = self.base_armor + bonus_armor
        armor -= armor * (self.armor_shred_percentage_modifiers.max() or 0)
        return armor

    def get_magic_resist(self):
        bonus_mr = self.flat_bonus_magic_resist_modifiers.sum()
        for item in self.items:
            bonus_mr += item.get_magic_resist_bonus()
        magic_resist = self.base_magic_resist + bonus_mr
        magic_resist -= magic_resist * (self.magic_resist_shred_percentage_modifiers.max() or 0)
        return magic_resist

    def get_dodge_chance(self):
        dodge = self.bonus_dodge
        for item in self.items:
            dodge += item.get_dodge_bonus()
        return dodge

    def can_cast_spell(self, map, time):
        return self.total_mana and self.mana >= self.get_effective_total_mana()

    def cast_spell(self, map, time):
        self.mana = 0
        self.percent_mana_increase = 0
        if self.cast_time:
            self.next_cast_spell_at = time + self.cast_time
        if self.mana_lock_time:
            self.mana_locked_until = time + self.mana_lock_time
        self.on_spell_cast()

    def on_spell_cast(self):
        self._MAP.on_spell_cast(self)
        for item in self.items:
            item.on_spell_cast(self)

    def perform_spell(self, map, time):
        raise NotImplementedError("This champion can't cast spell")

    def stun(self, time, stun_duration):
        if self.has_spell_shield:
            self.remove_spellshield_at_next_tick = True
            return
        if not self.has_stun_prevention_effect():
            self.stunned_until = max(self.stunned_until, time + stun_duration)

    def shroud(self, percent_mana_increase):
        self.percent_mana_increase = max(self.percent_mana_increase, percent_mana_increase)

    def get_effective_total_mana(self):
        return self.total_mana * (1 + self.percent_mana_increase / 100)

    def apply_hemoragy(self, time, hemoragy_duration):
        self.hemoragy_until = max(self.hemoragy_until, time + hemoragy_duration)

    def update_state_stunned(self, time):
        self.is_stunned = self.stunned_until > time

    def update_state_under_zephyr(self, time):
        self.is_under_zephyr = self.under_zephyr_until > time

    def update_state_under_revive(self, time):
        if not self.is_under_revive:
            return
        previously_under_revive = self.is_under_revive
        self.is_under_revive = time < self.under_revive_until
        if previously_under_revive and not self.is_under_revive:
            self.health = 0
            self.heal(self.revive_with)
            self.revive_with = 0
            self.is_stunned = False
            self.stunned_until = time - 1
            self.is_targetable = True
            self.untargetable_until = time - 1
            if self.has_revenant:
                self.percent_damage_reduction_modifiers.add_component('revenant', time, 9999, -25)
                self.innate_bonus_damage_multiplier_modifiers.add_component('revenant', time, 9999, 0.25)

    def update_state_hemoragy(self, time):
        self.has_hemoragy = self.hemoragy_until > time

    def update_state_targetable(self, time):
        self.is_targetable = self.untargetable_until is None or self.untargetable_until < time

    def update_state_mana_locked(self, time):
        previously_mana_locked = self.is_mana_locked
        self.is_mana_locked = self.mana_locked_until > time
        if previously_mana_locked and not self.is_mana_locked:
            for item in self.items:
                item.trigger_mana_lock_end(self)

    def update_state_spell_shield(self, time):
        if self.has_spell_shield and self.remove_spellshield_at_next_tick:
            self.has_spell_shield = False

    def update_states(self, time):
        self.update_state_stunned(time)
        self.update_state_hemoragy(time)
        self.update_state_targetable(time)
        self.update_state_mana_locked(time)
        self.update_state_under_revive(time)
        self.update_state_spell_shield(time)
        self.update_state_under_zephyr(time)
        self.update_modifiers(time)
        self.shield_manager.update_shields(time)

    def register_modifier(self, modifier):
        self._all_modifiers.append(modifier)

    def update_modifiers(self, time):
        for modifier in self._all_modifiers:
            modifier.update_components(time)

    def get_allies(self):
        return [u for u in self._MAP.units if u.team == self.team and u != self]

    def move_assassin(self, map, time):
        target_row = 7 if self.row <= 3 else 0
        target_col = self.col
        real_target_row, real_target_col = utils.closest_empty_tile_from_pos(target_row, target_col, map, farthest_from_row=self.row, farthest_from_col=self.col)
        self.move_to(real_target_row, real_target_col, MOVE_TIME_ASSASSIN)
        self.current_target = None

    def tick(self, map, time):
        self._MAP = map
        self._TIME = time

        for item in self.items:
            item.tick(self, map, time)

        self.update_states(time)

        for dot in self.dots:
            dot.update_state(time)
            dot.tick(map, time)

        self.on_hit_effects = [e for e in self.on_hit_effects if time <= e.expires_at]

        if self.is_under_revive or self.is_under_zephyr:
            return

        if not self.has_moved and Assassin in self.synergies:
            self.move_assassin(map, time)
        if self.is_moving and self.moves_until <= time:
            self.is_moving = False
        if self.current_target not in map.units or not self.current_target.is_targetable:
            self.current_target = None
        if self.current_target is None or self.last_attacked_at < time - 1:
            self.set_current_target(map)

        if self.is_stunned:
            pass  # stunned :'(
        elif self.next_cast_spell_at and time >= self.next_cast_spell_at:
            self.perform_spell(map, time)
            self.next_cast_spell_at = None
        elif self.next_cast_spell_at is None and self.can_cast_spell(map, time):
            self.cast_spell(map, time)
        elif not self.is_moving:  # Auto attack
            if self.current_target_is_in_range():
                next_attack_at = self.last_attacked_at + 1.0/self.get_attack_speed()
                if time >= next_attack_at and self.current_target:
                    self.aa_count += 1
                    if self.cannoneer_active and self.aa_count % 5 == 0:
                        self.launch_cannoneer_auto_attack(self.current_target, map, time)
                    else:
                        self.auto_attack(self.current_target, map, time)
                    self.last_attacked_at = time
            elif not self.is_moving and self.current_target is not None:
                self.move_towards_current_target(map, time)

    def closest_hex_enemy(self, map, for_first_target=False):
        enemies = [u for u in map.units if u.team != self.team and u.is_targetable]
        if for_first_target and self._TIME < 0.5:
            enemies = [u for u in enemies if Assassin not in u.synergies]
        if not enemies:
            return None
        return sorted(enemies, key=lambda e: self.xydistance2_with_unit(e))[0]

    def closest_hex_ally(self, map):
        allies = [u for u in map.units if u.team == self.team and u != self]
        if not allies:
            return None
        return sorted(allies, key=lambda u: self.xydistance2_with_unit(u))[0]

    def farthest_hex_enemy(self, map):
        enemies = [u for u in map.units if u.team != self.team and u.is_targetable]
        if not enemies:
            return None
        return sorted(enemies, key=lambda e: self.xydistance2_with_unit(e), reverse=True)[0]

    def farthest_hex_ally(self, map):
        allies = [u for u in map.units if u.team == self.team and u != self]
        if not allies:
            return None
        return sorted(allies, key=lambda u: self.xydistance2_with_unit(u), reverse=True)[0]

    def closest_empty_tile(self, map, farthest_from_row=None, farthest_from_col=None, closest_from_row=None, closest_from_col=None):
        return utils.closest_empty_tile_from_pos(self.row, self.col, map, farthest_from_row, farthest_from_col, closest_from_row, closest_from_col)

    def set_current_target(self, map, force=False):
        candidate_target = self.closest_hex_enemy(map, for_first_target=not self.has_had_target)
        if candidate_target is not None:
            self.has_had_target = True
            if self.current_target is None or self.current_target.distance(self.row, self.col) > candidate_target.distance(self.row, self.col):
                self.current_target = candidate_target

    def put_stack(self, stack_name, stack_count):
        if stack_name not in self.stacks:
            self.stacks[stack_name] = 0
        self.stacks[stack_name] += stack_count

    def get_critical_chance(self):
        critical_chance = self.base_critical_chance
        for item in self.items:
            critical_chance += item.get_critical_chance_bonus()
        return critical_chance

    def resolve_crit(self):
        return True if random.random() <= self.get_critical_chance() else False

    def has_crit_prevention_effect(self):
        return any(item.has_crit_prevention_effect() for item in self.items)

    def has_stun_prevention_effect(self):
        return any(item.has_stun_prevention_effect() for item in self.items)

    def has_spell_crit_effect(self):
        return any(item.has_spell_crit_effect() for item in self.items) or Assassin in self.synergies

    def has_miss_prevention_effect(self):
        return any(item.has_miss_prevention_effect() for item in self.items)

    def before_auto_attack(self, target, map, time):
        for item in self.items:
            item.before_auto_attack(self, target, map, time)

    def after_auto_attack(self, target, map, time):
        for item in self.items:
            item.after_auto_attack(self, target, map, time)

    def launch_cannoneer_auto_attack(self, target, map, time):
        self.before_auto_attack(target, map, time)
        self.increase_mana(self.mana_per_auto)
        damage = self.get_attack_damage() * self.cannoneer_ad_ratio
        for unit in map.units:
            if unit.team != target.team:
                continue
            if unit.distance(target.row, target.col) > 1:
                continue
            self.deal_physical_damage(unit, damage)
        self.after_auto_attack(target, map, time)

    def auto_attack(self, target, map, time, ad_ratio=1.0, apply_on_hit=True, apply_mana_increase=True, is_from_runaan=False, bonus_damage=0):
        if apply_on_hit and not is_from_runaan:
            self.before_auto_attack(target, map, time)
        if apply_mana_increase:
            self.increase_mana(self.mana_per_auto)
        damage = self.get_attack_damage() * ad_ratio + bonus_damage
        target_before_health = target.health
        damage, post_mitigation_damage = self.deal_physical_damage(target, damage)
        target.on_getting_aa_hit(map, time)
        for item in self.items:
            item.trigger_aa_damage_dealt(self, target, damage, post_mitigation_damage)
        if apply_on_hit:
            self.after_auto_attack(target, map, time)

    def on_getting_aa_hit(self, map, time):
        for item in self.items:
            item.on_getting_aa_hit(self, map, time)

    def on_damage_taken(self, damage_source, pre_mitigation_damage, post_mitigation_damage, damage_type):
        for item in self.items:
            item.on_damage_taken(self, damage_source, pre_mitigation_damage, post_mitigation_damage, damage_type)

    def has_item(self, item_cls):
        return any(type(item) == item_cls for item in self.items)

    def does_dodge(self):
        return random.random() <= self.get_dodge_chance()

    def enter_revive_state(self, time, revive_duration):
        self.health = 0
        self.dots = []
        self.under_revive_until = time + revive_duration
        self.untargetable_until = time + revive_duration
        self.is_under_revive = True

    def die(self, time):
        if self.revive_with:
            self.enter_revive_state(time, revive_duration=2)
        else:
            for item in self.items:
                item.trigger_on_death(self)
            self.is_dead = True
            if Hellion in self.synergies and not self.is_hellion_spawn and self.should_spawn_hellion:
                self.spawn_hellion()

    def spawn_hellion(self):
        spawn_time = 1
        hellion_unit = self.__class__(
            row=-1,
            col=-1,
            team=self.team,
            star_level=self.star_level - 1,
            items=[],
        )
        target_row, target_col = utils.closest_empty_tile_from_pos(self.row, self.col, self._MAP)
        hellion_unit.untargetable_until = self._TIME + spawn_time
        hellion_unit.move_to(target_row, target_col, self._TIME, spawn_time)
        hellion_unit.is_hellion_spawn = True
        self._MAP.spawn_unit(hellion_unit)

    def increase_mana(self, mana_increase):
        if self.is_mana_locked:
            return
        self.mana = min(self.get_effective_total_mana(), self.mana + mana_increase)

    def heal(self, heal_value):
        health_before = self.health
        if self.has_hemoragy:
            heal_value /= 2
        self.health = min(self.total_health, self.health + heal_value)
        self.on_health_changed(health_before)
        return heal_value - (self.health - health_before)

    def heal_with_overheal(self, heal_value, overheal_source_uuid, overheal_source_maximum):
        health_before = self.health
        excess_heal = self.heal(heal_value)
        if not self.shield_manager.has_shield(overheal_source_uuid):
            overheal_value = min(overheal_source_maximum, excess_heal)
        else:
            current_overheal = self.shield_manager.get_shield(overheal_source_uuid)
            overheal_value = min(overheal_source_maximum - current_overheal.value, excess_heal)
        if overheal_value > 0:
            self.shield_manager.add_shield_effect(self._TIME, overheal_value, 9999, shield_identifier=overheal_source_uuid)

    def increase_health(self, health_increase):
        self.health += health_increase
        self.total_health += health_increase

    def get_pre_mitigation_mana(self, damage):
        return 0.01 * damage

    def get_post_mitigation_mana(self, damage):
        return 0.07 * damage

    def increase_mana_after_damage(self, pre_mitigation_damage, post_mitigation_damage):
        self.increase_mana(
            min(
                self.get_pre_mitigation_mana(pre_mitigation_damage) + self.get_post_mitigation_mana(post_mitigation_damage),
                42.5
            )
        )

    def deal_physical_damage(self, target, base_damage, is_multitarget=False, can_crit=True):
        if not target:
            return 0, 0
        # print(self.image_name, 'of team', self.team, 'deals', base_damage, 'phy to', target.image_name, 'of team', target.team, 'with armor', target.get_armor())
        if not self.has_miss_prevention_effect() and target.does_dodge():
            return 0, 0

        damage = base_damage
        if can_crit and not target.has_crit_prevention_effect() and self.resolve_crit():
            damage *= self.get_cricical_damage()
            self.on_crit(target)
        damage = self.get_damage_after_multipliers(target, damage)
        # print('after multipliers', damage)
        damage, post_mitigation_damage = target.take_physical_damage(damage, self, is_multitarget=is_multitarget)
        for on_hit in self.on_hit_effects:
            on_hit.proc(target)
        self.trigger_damage_dealt_to_other(target, damage, post_mitigation_damage, type='physical')
        return damage, post_mitigation_damage

    def deal_magic_damage(self, target, base_damage, is_multitarget=False, can_crit=True, can_remove_spell_shield=True):
        if not target:
            return 0, 0
        # print(self.image_name, 'of team', self.team, 'deals', base_damage, 'mag to', target.image_name, 'of team', target.team)
        damage = base_damage
        if can_crit and self.has_spell_crit_effect() and not target.has_crit_prevention_effect() and self.resolve_crit():
            damage *= self.get_cricical_damage()
            self.on_crit(target)
        damage = self.get_damage_after_multipliers(target, damage)
        damage, post_mitigation_damage = target.take_magic_damage(
            damage,
            self,
            is_multitarget=is_multitarget,
            can_remove_spell_shield=can_remove_spell_shield
        )
        self.trigger_damage_dealt_to_other(target, damage, post_mitigation_damage, type='magic')
        return damage, post_mitigation_damage

    def deal_true_damage(self, target, base_damage, is_multitarget=False, can_crit=True, can_remove_spell_shield=True):
        if not target:
            return 0, 0
        # print(self.image_name, 'of team', self.team, 'deals', base_damage, 'true to', target.image_name, 'of team', target.team)
        damage = base_damage
        if can_crit and self.has_spell_crit_effect() and not target.has_crit_prevention_effect() and self.resolve_crit():
            damage *= self.get_cricical_damage()
            self.on_crit(target)
        damage = self.get_damage_after_multipliers(target, damage)
        damage, post_mitigation_damage = target.take_true_damage(
            damage,
            self,
            is_multitarget=is_multitarget,
            can_remove_spell_shield=can_remove_spell_shield
        )
        self.trigger_damage_dealt_to_other(target, damage, post_mitigation_damage, type='true')
        return damage, post_mitigation_damage

    def on_crit(self, target):
        for item in self.items:
            item.on_crit(self, target)

    def get_damage_after_multipliers(self, target, damage):
        bonus = self.innate_bonus_damage_multiplier_modifiers.sum()
        for item in self.items:
            bonus += item.get_bonus_damage_percentage(target, damage)
        return damage + (bonus * damage)

    def trigger_damage_dealt_to_other(self, target, damage, post_mitigation_damage, type):
        for item in self.items:
            item.trigger_damage_dealt_to_other(self, target, damage, post_mitigation_damage, type)
        if self.legionnaire_omnivamp_ratio:
            self.heal(post_mitigation_damage * self.legionnaire_omnivamp_ratio)

    def apply_flat_damage_reduction(self, damage):
        return max(0, damage - self.flat_damage_reduction_modifiers.sum())

    def apply_additional_percent_damage_reduction(self, damage, is_multitarget):
        percent_damage_reduction = self.percent_damage_reduction_modifiers.sum()
        if is_multitarget:
            percent_damage_reduction += self.multitarget_percent_damage_reduction_modifiers.sum()
        return damage - (damage * min(100, percent_damage_reduction) / 100)

    def take_physical_damage(self, damage, damage_source, is_multitarget=False):
        if self.is_under_revive or self.is_under_zephyr:
            return 0, 0
        # print('taking psy', damage)
        post_mitigation_damage = self.apply_flat_damage_reduction(
            self.apply_additional_percent_damage_reduction(
                self.apply_armor_reduction(damage), is_multitarget
            )
        )
        # print('reduced to', post_mitigation_damage)
        self._do_take_damage(post_mitigation_damage)
        self.increase_mana_after_damage(damage, post_mitigation_damage)
        self.on_damage_taken(damage_source, pre_mitigation_damage=damage, post_mitigation_damage=post_mitigation_damage, damage_type='physical')
        return damage, post_mitigation_damage

    def take_magic_damage(self, damage, damage_source, is_multitarget=False, can_remove_spell_shield=True):
        if self.is_under_revive or self.is_under_zephyr:
            return 0, 0
        if self.has_spell_shield and can_remove_spell_shield:
            self.remove_spellshield_at_next_tick = True
            return 0, 0
        post_mitigation_damage = self.apply_flat_damage_reduction(
            self.apply_additional_percent_damage_reduction(
                self.apply_magic_resist_reduction(damage), is_multitarget
            )
         )
        self._do_take_damage(post_mitigation_damage)
        self.increase_mana_after_damage(damage, post_mitigation_damage)
        self.on_damage_taken(damage_source, pre_mitigation_damage=damage, post_mitigation_damage=post_mitigation_damage, damage_type='magic')
        return damage, post_mitigation_damage

    def take_true_damage(self, damage, damage_source, is_multitarget=False, can_remove_spell_shield=True):
        if self.is_under_revive or self.is_under_zephyr:
            return 0, 0
        if self.has_spell_shield and can_remove_spell_shield:
            self.remove_spellshield_at_next_tick = True
            return 0, 0
        self._do_take_damage(damage)
        self.increase_mana_after_damage(damage, damage)
        self.on_damage_taken(damage_source, pre_mitigation_damage=damage, post_mitigation_damage=damage, damage_type='true')
        return damage, damage

    def apply_armor_reduction(self, damage):
        percentage = self.get_armor()/(self.get_armor() + 100)
        return damage - percentage * damage

    def apply_magic_resist_reduction(self, damage):
        percentage = self.get_magic_resist()/(self.get_magic_resist() + 100)
        damage_after_mr = damage - percentage * damage
        for item in self.items:
            damage_after_mr = item.apply_additional_magic_reduction(damage_after_mr)
        return damage_after_mr

    def _do_take_damage(self, damage):
        # print(self.image_name, 'of team', self.team, 'takes', damage)
        damage = self.shield_manager.absorb_and_return_remaining_damage(damage)
        health_before = self.health
        self.health -= damage
        if damage:
            self.on_health_changed(health_before)

    def on_health_changed(self, health_before):
        for item in self.items:
            item.on_health_changed(self, health_before)

    def distance(self, row, col):
        return utils.distance(self.row, self.col, row, col)

    def xydistance2_with_unit(self, unit):
        x, y = utils.xy_pos_from_ij_tile(unit.row, unit.col)
        return self.xydistance2_with_point(x, y)

    def xydistance2_with_point(self, x, y):
        x1, y1 = utils.xy_pos_from_ij_tile(self.row, self.col)
        return (x-x1)**2 + (y-y1)**2

    def current_target_is_in_range(self):
        return self.current_target and self.distance(self.current_target.row, self.current_target.col) <= self.attack_range

    def move_towards_current_target(self, map, time):
        backtrack = {}
        Q = deque()
        visited = set()
        Q.append((self.row, self.col))
        while Q:
            row, col = Q.popleft()
            visited.add((row, col))
            neighbours = utils.get_neighbours(row, col)
            random.shuffle(neighbours)
            for neighbour in neighbours:
                nr, nc = neighbour[0], neighbour[1]
                if (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                if nr == self.current_target.row and nc == self.current_target.col:
                    if Cavalier in self.synergies:
                        self.move_to(row, col, time)
                        if self.percent_damage_reduction_modifiers.get_component('cavalier_background'):
                            self.percent_damage_reduction_modifiers.add_component(
                                'cavalier_charge', time, 4, self.percent_damage_reduction_modifiers.get_component('cavalier_background')[1]
                            )
                    else:
                        curr = (row, col)
                        while backtrack[curr] != (self.row, self.col):
                            curr = backtrack[curr]
                        self.move_to(curr[0], curr[1], time)
                        return
                if any(unit.row == nr and unit.col == nc for unit in map.units):
                    continue
                backtrack[(nr, nc)] = (row, col)
                Q.append((nr, nc))

    def move_to(self, row, col, time, move_time=MOVE_TIME):
        self.row = row
        self.col = col
        self.is_moving = True
        self.has_moved = True
        self.moves_until = time + move_time

    def draw(self, screen, time):
        base_tile_pos = utils.xy_pos_from_ij_tile(self.row, self.col)
        screen.blit(self.image, (base_tile_pos[0] + 10, base_tile_pos[1] + 10))

    def draw2(self, screen, time):
        base_tile_pos = utils.xy_pos_from_ij_tile(self.row, self.col)

        health_ratio = self.health / self.total_health
        shield_ratio = self.shield_manager.get_total_shield_value() / self.total_health
        health_width = UNIT_IMAGE_WIDTH * health_ratio
        shield_width = UNIT_IMAGE_WIDTH * shield_ratio
        mana_ratio = self.mana / self.get_effective_total_mana() if self.total_mana else 0
        mana_ratio = min(mana_ratio, 1)
        mana_width = UNIT_IMAGE_WIDTH * mana_ratio
        health_color = (0, 255, 0) if self.team == 1 else (255, 0, 0)
        mana_color = (0, 0, 255) if not self.percent_mana_increase else (125, 125, 125)
        pygame.draw.rect(screen, health_color, (base_tile_pos[0]+10, base_tile_pos[1]+50, health_width, 10))
        pygame.draw.rect(screen, (255, 255, 255), (base_tile_pos[0]+10+health_width, base_tile_pos[1]+50, shield_width, 10))
        pygame.draw.rect(screen, mana_color, (base_tile_pos[0]+10, base_tile_pos[1]+60, mana_width, 10))

        stars_pos = []
        if self.star_level == 1:
            stars_pos = [base_tile_pos[0] + 30]
        if self.star_level == 2:
            stars_pos = [base_tile_pos[0] + 20, base_tile_pos[0] + 40]
        if self.star_level == 3:
            stars_pos = [base_tile_pos[0] + 10, base_tile_pos[0] + 30, base_tile_pos[0] + 50]

        for star_pos in stars_pos:
            screen.blit(star_image, (star_pos, base_tile_pos[1]))

        for i, item in enumerate(self.items):
            screen.blit(item.image, (base_tile_pos[0] + 10 + i*20, base_tile_pos[1] + 30))

        if self.is_under_zephyr:
            screen.blit(font.render('ZEPHYR', False, (255, 0, 0)), (base_tile_pos[0] + 10, base_tile_pos[1] + 30))
        if self.has_spell_shield:
            screen.blit(font.render('SHIELD', False, (0, 255, 0)), (base_tile_pos[0] + 10, base_tile_pos[1] + 30))
        elif self.is_under_revive:
            screen.blit(font.render('REVIVE', False, (0, 0, 255)), (base_tile_pos[0] + 10, base_tile_pos[1] + 30))
        elif self.is_stunned:
            screen.blit(font.render('STUNNED', False, (255, 0, 0)), (base_tile_pos[0] + 10, base_tile_pos[1] + 30))

    def fiddle_crowstorm_extend(self, unit):
        pass