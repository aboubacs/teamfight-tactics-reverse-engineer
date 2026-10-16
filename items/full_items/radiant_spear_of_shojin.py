import pygame

from items.item import Item

class RadiantSpearOfShojin(Item):
    def __init__(self):
        super().__init__('radiant_spear_of_shojin')

    def trigger_on_add(self, map, unit):
        unit.increase_mana(15)
        unit.mana_per_auto += 15

    def get_attack_damage_bonus(self):
        return 10