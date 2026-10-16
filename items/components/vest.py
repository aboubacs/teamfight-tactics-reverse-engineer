import pygame

from items.item import Item

class Vest(Item):
    def __init__(self):
        super().__init__('vest')

    def get_armor_bonus(self):
        return 20