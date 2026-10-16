import pygame

from items.item import Item

class GargoyleStoneplate(Item):
    def __init__(self):
        super().__init__('gargoyle_stoneplate')
        self.total_enemies_targetting_holder = 0
        self.bonus_per_stack = 18

    def get_armor_bonus(self):
        return 20 + self.bonus_per_stack * (self.total_enemies_targetting_holder)

    def get_magic_resist_bonus(self):
        return 20 + self.bonus_per_stack * (self.total_enemies_targetting_holder)

    def tick(self, unit, map, time):
        self.total_enemies_targetting_holder = 0
        for u in map.units:
            if u.team != unit.team and u.current_target == unit:
                self.total_enemies_targetting_holder += 1