import pygame

from items.item import Item

class BF(Item):
    def __init__(self):
        super().__init__('bf')

    def get_attack_damage_bonus(self):
        return 10