import pygame

from items.item import Item

class RadiantBloodThirster(Item):
    def __init__(self):
        super().__init__('radiant_bloodthirster')
        self.shield_triggered = False

    def get_attack_damage_bonus(self):
        return 10 + 30

    def get_magic_resist_bonus(self):
        return 20

    def trigger_aa_damage_dealt(self, unit, target, damage_before_mitigation, post_mitigation_damage):
        unit.heal(0.50 * post_mitigation_damage)

    def on_health_changed(self, unit, health_before):
        if not self.shield_triggered and unit.health < 0.4 * unit.total_health:
            self.shield_triggered = True
            unit.add_shield_effect(shield_value=0.6*unit.total_health, shield_duration=5)