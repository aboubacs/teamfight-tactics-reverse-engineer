import pygame

from items.item import Item

class Bow(Item):
    def __init__(self):
        super().__init__('bow')

    def get_attack_speed_bonus(self):
        return 0.10