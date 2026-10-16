import pygame

from items.item import Item

class BlueBuff(Item):
    def __init__(self):
        super().__init__('blue_buff')

    def trigger_on_add(self, map, unit):
        unit.increase_mana(30)
    
    def trigger_mana_lock_end(self, unit):
        unit.increase_mana(20)