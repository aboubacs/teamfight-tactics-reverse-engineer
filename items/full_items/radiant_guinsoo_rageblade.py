import uuid
import pygame

from items.item import Item

class RadiantGuinsooRageblade(Item):
    def __init__(self):
        super().__init__('radiant_guinsoo_rageblade')
        self.nb_auto_attacks = 0
        self.bonus_attack_speed_per_stack = 0.09  # TODO: check value ??

    def get_attack_speed_bonus(self):
        return 0.10 + 0.30 + self.bonus_attack_speed_per_stack * self.nb_auto_attacks

    def get_spell_power_bonus(self):
        return 10

    def before_auto_attack(self, unit, target, map, time):
        self.nb_auto_attacks += 1