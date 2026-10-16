import pygame

from items.item import Item

class GiantSlayer(Item):
    def __init__(self):
        super().__init__('giant_slayer')

    def get_attack_speed_bonus(self):
        return 0.10

    def get_attack_damage_bonus(self):
        return 10

    def get_bonus_damage_percentage(self, target, damage):
        if target.total_health > 1650:
            return 0.75
        return 0.1