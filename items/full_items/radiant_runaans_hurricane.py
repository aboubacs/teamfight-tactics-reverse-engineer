import pygame

from items.item import Item

class RadiantRunaansHurricane(Item):
    def __init__(self):
        super().__init__('radiant_runaans_hurricane')

    def get_attack_speed_bonus(self):
        return 0.10 + 0.30

    def get_magic_resist_bonus(self):
        return 20

    def get_target(self, map, unit):
        target = None
        target_distance = None
        for u in map.units:
            if u.team != unit.team and u != unit.current_target:
                if target is None or unit.distance(u.row, u.col) < target_distance:
                    target = u
                    target_distance = unit.distance(u.row, u.col)
        return target

    def before_auto_attack(self, unit, target, map, time):
        target = self.get_target(map, unit)
        if target:
            unit.auto_attack(target, map, time, ad_ratio=1.10, apply_on_hit=True, apply_mana_increase=False, is_from_runaan=True)