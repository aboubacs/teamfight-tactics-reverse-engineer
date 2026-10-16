import pygame

from units.unit import Unit

class TahmKench(Unit):
    def __init__(self, **kwargs):
        super().__init__(
            cost=1,
            health=700,
            starting_mana=0,
            total_mana=0,
            armor=40,
            magic_resist=30,
            attack_damage=85,
            attack_speed=0.5,
            attack_range=1,
            image_name='tahm_kench',
            **kwargs,
        )

    def _do_take_damage(self, damage):
        self.health -= (damage - self.get_damage_reduction())

    def get_damage_reduction(self):
        base_reduction = {
            1: 15,
            2: 25,
            3: 75
        }[max(1, self.star_level)]
        return base_reduction * self.get_spell_power() / 100