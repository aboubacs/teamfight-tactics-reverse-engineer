import pygame

from items.item import Item

class JeweledGauntlet(Item):
    def __init__(self):
        super().__init__('jeweled_gauntlet')
        
    def get_spell_power_bonus(self):
        return 10
    
    def get_critical_chance_bonus(self):
        return 0.15

    def get_critical_damage_bonus(self, unit):
        return 0.40

    def has_spell_crit_effect(self):
        return True