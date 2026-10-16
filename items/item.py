import pygame
import uuid

class Item:
    def __init__(self, image_name):
        self.image_name = image_name
        self.image = pygame.image.load('./images/' + self.image_name + '.png')
        self.image = pygame.transform.smoothscale(self.image, (20, 20))
        self.uuid = uuid.uuid4()

    def get_attack_speed_bonus(self):
        return 0

    def get_attack_damage_bonus(self):
        return 0

    def get_armor_bonus(self):
        return 0

    def get_magic_resist_bonus(self):
        return 0

    def get_dodge_bonus(self):
        return 0

    def get_critical_chance_bonus(self):
        return 0

    def get_critical_damage_bonus(self, unit):
        return 0

    def get_spell_power_bonus(self):
        return 0

    def trigger_on_add(self, map, unit):
        pass

    def trigger_on_death(self, unit):
        pass

    def trigger_aa_damage_dealt(self, unit, target, damage_before_mitigation, post_mitigation_damage):
        pass

    def trigger_damage_dealt_to_other(self, unit, target, damage_before_mitigation, post_mitigation_damage, type):
        pass

    def trigger_mana_lock_end(self, unit):
        pass

    def on_getting_aa_hit(self, unit, map, time):
        pass

    def apply_additional_magic_reduction(self, damage):
        return damage

    def tick(self, unit, map, time):
        pass

    def on_crit(self, unit, target):
        pass

    def get_bonus_damage_percentage(self, target, damage):
        return 0

    def before_auto_attack(self, unit, target, map, time):
        pass

    def after_auto_attack(self, unit, target, map, time):
        pass

    def on_health_changed(self, unit, health_before):
        pass

    def has_crit_prevention_effect(self):
        return False

    def has_stun_prevention_effect(self):
        return False

    def has_spell_crit_effect(self):
        return False

    def has_miss_prevention_effect(self):
        return False

    def on_spell_cast(self, unit):
        pass

    def on_damage_taken(self, unit, damage_source, pre_mitigation_damage, post_mitigation_damage, damage_type):
        pass

    def get_zap_mana_percentage_value(self):
        return 0