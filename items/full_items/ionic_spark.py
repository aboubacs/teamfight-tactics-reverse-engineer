import pygame

from items.item import Item

class IonicSpark(Item):
    def __init__(self):
        super().__init__('ionic_spark')
        self.range = 2

    def get_magic_resist_bonus(self):
        return 20

    def get_spell_power_bonus(self):
        return 10

    def tick(self, unit, map, time):
        for u in map.units:
            if u.team != unit.team and u.distance(unit.row, unit.col) <= self.range:
                u.magic_resist_shred_percentage_modifiers.add_component(self.uuid, time, 0.5, 0.5)

    def get_zap_mana_percentage_value(self):
        return 250