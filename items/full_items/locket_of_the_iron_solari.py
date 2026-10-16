import pygame

from items.item import Item

class LocketOfTheIronSolari(Item):
    def __init__(self):
        super().__init__('locket_of_the_iron_solari')
        
    def get_spell_power_bonus(self):
        return 10
    
    def get_armor_bonus(self):
        return 20

    def get_shield_value(self, unit):
        return {
            1: 300,
            2: 350,
            3: 400
        }[unit.star_level]

    def trigger_on_add(self, map, unit):
        for u in map.units:
            if u.team == unit.team and u.row == unit.row and abs(u.col - unit.col) <= 2:
                u.add_shield_effect(shield_value=self.get_shield_value(unit), shield_duration=8)