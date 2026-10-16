import pygame

from items.item import Item

class RadiantGargoyleStoneplate(Item):
    def __init__(self):
        super().__init__('radiant_gargoyle_stoneplate')
        self.total_enemies_targetting_holder = 0
        self.last_triggered_at = 0
        self.bonus_per_stack = 40

    def get_armor_bonus(self):
        return 20 + self.bonus_per_stack * (self.total_enemies_targetting_holder)

    def get_magic_resist_bonus(self):
        return 20 + self.bonus_per_stack * (self.total_enemies_targetting_holder)

    def tick(self, unit, map, time):
        self.total_enemies_targetting_holder = 0
        for u in map.units:
            if u.team != unit.team and u.current_target == unit:
                self.total_enemies_targetting_holder += 1
        if time >= self.last_triggered_at + 1:
            self.last_triggered_at = time
            unit.heal(0.02 * unit.total_health)