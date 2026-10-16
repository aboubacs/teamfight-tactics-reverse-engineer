import pygame

from items.item import Item

class Gloves(Item):
    def __init__(self):
        super().__init__('gloves')

    def get_critical_chance_bonus(self):
        return 0.05

    def get_dodge_bonus(self):
        return 0.10