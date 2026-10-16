import pygame

from items.item import Item

class Belt(Item):
    def __init__(self):
        super().__init__('belt')

    def trigger_on_add(self, map, unit):
        unit.increase_health(150)