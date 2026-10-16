import pygame

from items.item import Item

class RadiantChalice(Item):
    def __init__(self):
        super().__init__('radiant_chalice')

    def trigger_on_add(self, map, unit):
        unit.increase_mana(15)

        for u in map.units:
            if u.team == unit.team and u.row == unit.row and abs(u.col - unit.col) <= 1:
                u.spell_power += 50

    def get_magic_resist_bonus(self):
        return 20