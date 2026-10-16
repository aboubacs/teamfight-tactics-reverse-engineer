import pygame

from items.item import Item

class RadiantInfinityEdge(Item):
    def __init__(self):
        super().__init__('radiant_infinity_edge')

    def get_attack_damage_bonus(self):
        return 10
    
    def get_critical_chance_bonus(self):
        return 0.75

    def get_critical_damage_bonus(self, unit):
        return max(0, unit.get_critical_chance() - 1) + 0.40
