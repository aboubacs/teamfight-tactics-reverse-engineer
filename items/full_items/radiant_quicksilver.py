import pygame

from items.item import Item

class RadiantQuicksilver(Item):
    def __init__(self):
        super().__init__('radiant_quicksilver')
        self.time = 0

    def get_dodge_bonus(self):
        return 0.15

    def get_magic_resist_bonus(self):
        return 20

    def tick(self, unit, map, time):
        self.time = time

    def has_stun_prevention_effect(self):
        return self.time <= 30

    def get_attack_speed_bonus(self):
        return 0.40