import pygame

from items.item import Item

class Tear(Item):
    def __init__(self):
        super().__init__('tear')

    def trigger_on_add(self, map, unit):
        unit.increase_mana(15)