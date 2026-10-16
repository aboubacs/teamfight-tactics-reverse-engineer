import pygame

from items.item import Item

class Cloak(Item):
    def __init__(self):
        super().__init__('cloak')

    def get_magic_resist_bonus(self):
        return 20