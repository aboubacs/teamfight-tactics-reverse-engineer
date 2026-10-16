import pygame

from items.item import Item

class RadiantRadabonsDeathcap(Item):
    def __init__(self):
        super().__init__('radiant_rabadons_deathcap')

    def get_spell_power_bonus(self):
        return 120