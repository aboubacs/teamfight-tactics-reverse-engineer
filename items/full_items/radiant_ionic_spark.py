import pygame

from items.item import Item

class RadiantIonicSpark(Item):
    def __init__(self):
        super().__init__('radiant_ionic_spark')
        self.range = 4
        self.last_triggered_at = 0

    def get_magic_resist_bonus(self):
        return 20

    def get_spell_power_bonus(self):
        return 10

    def tick(self, unit, map, time):
        for u in map.units:
            if u.team != unit.team and u.distance(unit.row, unit.col) <= self.range:
                u.magic_resist_shred_percentage_modifiers.add_component(self.uuid, time, 0.5, 0.5)
        if time >= self.last_triggered_at + 1:
            self.last_triggered_at = time
            unit.heal(0.01 * unit.total_health)

    def get_zap_mana_percentage_value(self):
        return 300