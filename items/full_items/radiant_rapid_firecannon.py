import pygame

from items.item import Item

class RadiantRapidFirecannon(Item):
    def __init__(self):
        super().__init__('radiant_rapid_firecannon')

    def get_attack_speed_bonus(self):
        return 0.40 + 0.20

    def has_miss_prevention_effect(self):
        return True

    def trigger_on_add(self, map, unit):
        unit.attack_range += 2