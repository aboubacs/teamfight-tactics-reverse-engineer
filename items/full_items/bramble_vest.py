import pygame

from items.item import Item

# TODO: spell crit prevention
class BrambleVest(Item):
    def __init__(self):
        super().__init__('bramble')
        self.last_aoe_tick = None

    def get_armor_bonus(self):
        return 40

    def get_aoe_magic_damage(self, unit):
        return {
            1: 80,
            2: 100,
            3: 150
        }[unit.star_level]

    def on_getting_aa_hit(self, unit, map, time):
        if self.last_aoe_tick is None or self.last_aoe_tick + 2.5 <= time:
            for u in map.units:
                if u.team != unit.team and u.distance(unit.row, unit.col) <= 1:
                    # don't use unit.deal because there is no modifier/effect
                    u.take_magic_damage(self.get_aoe_magic_damage(unit), unit)
        self.last_aoe_tick = time

    def has_crit_prevention_effect(self):
        return True