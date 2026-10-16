import copy
import random
import utils

from synergies.synergy import Synergy
from projectile import Projectile

class AboRush(Projectile):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.units_hit = 0

    def on_unit_hit(self, time, unit):
        if unit.team == self.owner.team:
            return

        self.units_hit += 1
        self.owner.monstrosity.deal_physical_damage(unit, self.owner.get_charge_damage())
        unit.stun(time, 1)
        if self.units_hit >= 2:
            self.destroyed = True

    def compute_arrival_rc(self, board, time):
        x, y = self.get_xy_pos(time)
        r, c = utils.rc_from_xy(x, y)
        tr, tc = self.owner.get_tomb_rowcol()
        return utils.closest_empty_tile_from_pos(r, c, board, closest_from_row=tr, closest_from_col=tc)

    def on_destroy(self, board, time):
        row, col = self.compute_arrival_rc(board, time)
        self.owner.monstrosity.row = row
        self.owner.monstrosity.col = col

        for unit in board.units:
            if unit.team != self.owner.team and unit.distance(row, col) <= 1:
                self.owner.monstrosity.deal_magic_damage(unit, self.owner.get_crash_damage())

        board.spawn_unit(self.owner.monstrosity)


class Abomination(Synergy):
    steps = [3, 4, 5]

    def __init__(self, activated_step, **kwargs):
        super().__init__(activated_step)
        self.monstrosity_cls = kwargs.get('monstrosity_cls')

    def get_monstrosity_base_health(self):
        return {
            3: 900,
            4: 1400,
            5: 1900,
        }[self.activated_step]

    def get_monstrosity_base_ad(self):
        return {
            3: 70,
            4: 80,
            5: 90,
        }[self.activated_step]

    def get_monstrosity_armor(self):
        return {
            3: 40,
            4: 50,
            5: 60,
        }[self.activated_step]

    def get_monstrosity_magic_resist(self):
        return {
            3: 40,
            4: 50,
            5: 60,
        }[self.activated_step]

    def get_monstrosity_health_per_stack(self):
        return {
            3: 90,
            4: 140,
            5: 190,
        }[self.activated_step]

    def get_monstrosity_ad_per_stack(self):
        return {
            3: 7,
            4: 8,
            5: 9,
        }[self.activated_step]

    def get_crash_damage(self):
        return {
            3: 150,
            4: 200,
            5: 250,
        }[self.activated_step] * self.monstrosity.get_spell_power() / 100

    def get_charge_damage(self):
        return 350 * self.monstrosity.get_spell_power() / 100

    def get_target_unit(self, board):
        enemies = [u for u in board.units if u.team != self.team and u.is_targetable]
        if not enemies:
            return
        tx, ty = self.get_tomb_xy()
        return sorted(enemies, key=lambda e: e.xydistance2_with_point(tx, ty), reverse=True)[0]

    def on_death(self, board, time, death_count):
        if death_count != 2:
            return

        tx, ty = self.get_tomb_xy()

        target_unit = self.get_target_unit(board)
        if target_unit:
            xE, yE = utils.xy_pos_from_ij_tile(target_unit.row, target_unit.col)
        else:
            xE, yE = tx + 1, ty + 1

        board.projectiles.append(
            AboRush(
                map=board,
                owner=self,
                time=time,
                x0=tx,
                y0=ty,
                xE=xE,
                yE=yE,
                radius=30,
                hex_per_second=8,
            )
        )

    def get_tomb_rowcol(self):
        if self.first_rows:
            return (1, 6)
        else:
            return (6, 0)

    def get_tomb_xy(self):
        r, c = self.get_tomb_rowcol()
        return utils.xy_pos_from_ij_tile(r, c)

    def on_start_fight(self, units):
        abo_units = [u for u in units if self.__class__ in u.synergies]
        stacks = sum([u.star_level for u in abo_units])

        self.team = 1 if units[0].team == 1 else 2
        self.first_rows = True if units[0].row <= 3 else False
        tx, ty = self.get_tomb_xy()
        tr, tc = self.get_tomb_rowcol()
        closest_units = sorted(
            abo_units,
            key=lambda u: u.xydistance2_with_point(tx, ty)
        )

        items = []
        for u in closest_units:
            if len(items) == 3:
                continue
            if u.items:
                items.append(copy.copy(random.choice(u.items)))

        self.monstrosity = self.monstrosity_cls(
            health=self.get_monstrosity_base_health() + self.get_monstrosity_health_per_stack() * stacks,
            armor=self.get_monstrosity_armor(),
            magic_resist=self.get_monstrosity_magic_resist(),
            attack_damage=self.get_monstrosity_base_ad() + self.get_monstrosity_ad_per_stack() * stacks,
            items=items,
            row=tr,
            col=tc,
            team=self.team,
        )