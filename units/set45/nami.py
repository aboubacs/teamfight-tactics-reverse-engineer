import pygame

from units.unit import Unit

class Nami(Unit):
    def __init__(self, **kwargs):
        super().__init__(
            cost=1,
            health=550,
            starting_mana=40,
            total_mana=80,
            armor=20,
            magic_resist=20,
            attack_damage=40,
            attack_speed=0.65,
            attack_range=3,
            image_name='nami',
            **kwargs,
        )
        self.cast_time = 0.4
        self.spell_target = None

    def get_aqua_prison_damage(self):
        base_damage = {
            1: 225,
            2: 325,
            3: 450
        }[max(1, self.star_level)]
        return base_damage * self.get_spell_power() / 100

    def get_aqua_prison_stun_duration(self):
        base_stun_duration = {
            1: 2.5,
            2: 3,
            3: 4
        }[max(1, self.star_level)]
        return base_stun_duration

    def cast_spell(self, map, time):
        super().cast_spell(map, time)
        self.spell_target = self.closest_hex_enemy(map)
        
    def perform_spell(self, map, time):
        self.deal_magic_damage(self.spell_target, self.get_aqua_prison_damage())
        self.spell_target.stun(time, self.get_aqua_prison_stun_duration())