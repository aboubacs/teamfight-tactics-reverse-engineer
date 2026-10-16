import pygame

from items.item import Item

class Rod(Item):
    def __init__(self):
        super().__init__('rod')

    def get_spell_power_bonus(self):
        return 10