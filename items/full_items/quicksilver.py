import pygame

from items.item import Item

class Quicksilver(Item):
    def __init__(self):
        super().__init__('quicksilver')
        self.time = 0

    def get_dodge_bonus(self):
        return 0.15

    def get_magic_resist_bonus(self):
        return 20

    def tick(self, unit, map, time):
        self.time = time

    def has_stun_prevention_effect(self):
        return self.time <= 15