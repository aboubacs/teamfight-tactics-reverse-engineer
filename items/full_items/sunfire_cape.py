import pygame
import random

from items.item import Item

from dot import Dot

class SunfireCapeBurn(Dot):
    def is_burn_dot(self):
        return True

    def trigger(self, map, time):
        self.owner.deal_true_damage(
            self.unit,
            self.unit.total_health * 2.5 / 100,
            can_crit=False,
            can_remove_spell_shield=False
        )

class SunfireCape(Item):
    def __init__(self):
        super().__init__('sunfire_cape')
        self.last_tick_at = -9999
        self.tick_period = 2.5
        self.tick_range = 2

    def trigger_on_add(self, map, unit):
        unit.increase_health(150)

    def get_armor_bonus(self):
        return 20

    def tick(self, unit, map, time):
        if time >= self.last_tick_at + self.tick_period:
            targets_in_range = [
                u for u in map.units
                if u.team != unit.team and u.distance(unit.row, unit.col) <= self.tick_range and (
                    not any([dot.is_burn_dot() for dot in u.dots])
                )
            ]
            if targets_in_range:
                self.last_tick_at = time
                target = random.choice(targets_in_range)
                target.apply_hemoragy(time, 10)
                target.dots.append(
                    SunfireCapeBurn(
                        owner=unit,
                        unit=target,
                        time=time,
                        trigger_delay=1,
                        trigger_duration=8,
                    )
                )
