import pygame

from items.item import Item

class Deathblade(Item):
    def __init__(self):
        super().__init__('deathblade')
        self.targets = set()
        self.stack_damage = 10
        self.starting_stacks = 4

    def get_attack_damage_bonus(self):
        return 20 + self.stack_damage * (self.starting_stacks + self.get_bonus_stacks())

    def get_bonus_stacks(self):
        return len([u for u in self.targets if u.is_dead])

    def trigger_damage_dealt_to_other(self, unit, target, damage_before_mitigation, post_mitigation_damage, type):
        self.targets.add(target)