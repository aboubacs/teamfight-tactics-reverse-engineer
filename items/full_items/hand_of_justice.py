import random
import pygame

from items.item import Item

class HandOfJustice(Item):
    def __init__(self):
        super().__init__('hand_of_justice')
        self.mode_damage = random.random() >= 0.5

    def get_critical_chance_bonus(self):
        return 0.15

    def get_attack_damage_bonus(self):
        return 35 if self.mode_damage else 10

    def get_spell_power_bonus(self):
        return 35 if self.mode_damage else 10

    def trigger_on_add(self, map, unit):
        unit.increase_mana(15)

    def trigger_damage_dealt_to_other(self, unit, target, damage_before_mitigation, post_mitigation_damage, type):
        unit.heal((0.10 if self.mode_damage else 0.35) * post_mitigation_damage)