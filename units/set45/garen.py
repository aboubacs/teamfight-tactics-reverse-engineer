import pygame

from units.unit import Unit

class Garen(Unit):
    def __init__(self, **kwargs):
        super().__init__(
            cost=1,
            health=600,
            starting_mana=100,
            total_mana=170,
            armor=50,
            magic_resist=35,
            attack_damage=50,
            attack_speed=0.6,
            attack_range=1,
            image_name='garen',
            **kwargs,
        )

    def get_god_lions_justice_max_health_damage_ratio(self):
        base_damage = {
            1: 0.25,
            2: 0.35,
            3: 2
        }[max(1, self.star_level)]
        return base_damage * self.get_spell_power() / 100

    def get_god_lions_justice_max_health_shield_ratio(self):
        return {
            1: 0.4,
            2: 0.55,
            3: 2.0
        }[max(1, self.star_level)] * self.get_spell_power() / 100

    def perform_spell(self, board, time):
        target = self.current_target or self.closest_hex_enemy(board)
        if not target:
            return

        self.add_shield_effect(shield_value=self.get_god_lions_justice_max_health_shield_ratio() * self.total_health, shield_duration=5)

        for enemy in self.enemies(board):
            if enemy.distance(target.row, target.col) <= 3:
                enemy.magic_resist_shred_percentage_modifiers.add_component(self.uuid, time, 8, 0.5)
                self.deal_magic_damage(enemy, enemy.total_health * self.get_god_lions_justice_max_health_damage_ratio())
