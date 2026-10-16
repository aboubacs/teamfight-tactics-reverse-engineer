import pygame

from items.item import Item

class WarmogsArmor(Item):
    def __init__(self):
        super().__init__('warmogs_armor')

    def trigger_on_add(self, map, unit):
        unit.increase_health(1000)