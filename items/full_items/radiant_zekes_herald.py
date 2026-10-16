import pygame

from items.item import Item

class RadiantZekesHerald(Item):
    def __init__(self):
        super().__init__('radiant_zekes_herald')

    def get_attack_damage_bonus(self):
        return 10

    def trigger_on_add(self, map, unit):
        unit.increase_health(150)
        for u in map.units:
            if u.team == unit.team and u.row == unit.row and abs(u.col - unit.col) <= 1:
                u.base_attack_speed_bonus_ratio_modifiers.add_component(self.uuid, 0, 9999, 0.50)
