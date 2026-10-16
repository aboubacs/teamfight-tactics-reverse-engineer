import pygame

from items.item import Item

class RadiantBlueBuff(Item):
    def __init__(self):
        super().__init__('radiant_blue_buff')

    def trigger_on_add(self, map, unit):
        unit.increase_mana(30)

    def get_spell_power_bonus(self):
        return 40

    def trigger_mana_lock_end(self, unit):
        unit.increase_mana(30)