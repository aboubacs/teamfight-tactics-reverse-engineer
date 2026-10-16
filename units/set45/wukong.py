import pygame

from units.unit import Unit

class Wukong(Unit):
    def __init__(self, **kwargs):
        super().__init__(
            cost=1,
            health=650,
            starting_mana=0,
            total_mana=50,
            armor=40,
            magic_resist=30,
            attack_damage=55,
            attack_speed=0.65,
            attack_range=1,
            image_name='wukong',
            **kwargs,
        )
        self.cast_time = 0.2

    def get_crushing_blow_damage_multiplier(self):
        base_damage = {
            1: 2.25,
            2: 2.50,
            3: 2.70
        }[max(1, self.star_level)]
        return base_damage * self.get_spell_power() / 100

    def get_crushing_blow_stun_duration(self):
        base_stun_duration = {
            1: 1.5,
            2: 2.5,
            3: 3
        }[max(1, self.star_level)]
        return base_stun_duration
        
    def get_crushing_blow_damage(self):
        return self.get_crushing_blow_damage_multiplier() * self.get_attack_damage()

    def perform_spell(self, map, time):
        if self.current_target is None:
            return  # oops, canceled :'(
        if self.current_target.does_dodge():
            return
        self.deal_physical_damage(self.current_target, self.get_crushing_blow_damage())
        self.current_target.stun(time, self.get_crushing_blow_stun_duration())