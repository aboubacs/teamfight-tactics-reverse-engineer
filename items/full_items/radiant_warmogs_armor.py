import pygame

from items.item import Item

class RadiantWarmogsArmor(Item):
    def __init__(self):
        super().__init__('radiant_warmogs_armor')
        self.last_triggered_at = 0

    def trigger_on_add(self, map, unit):
        unit.increase_health(1800)

    def tick(self, unit, map, time):
        if time >= self.last_triggered_at + 1:
            self.last_triggered_at = time
            unit.heal(0.01 * unit.total_health)