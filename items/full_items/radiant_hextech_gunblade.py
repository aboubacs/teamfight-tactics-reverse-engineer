import pygame
import uuid 

from items.item import Item

class RadiantHextechGunblade(Item):
    def __init__(self):
        super().__init__('radiant_hextech_gunblade')
        self.uuid = uuid.uuid4()

    def get_spell_power_bonus(self):
        return 10 + 30

    def get_attack_damage_bonus(self):
        return 10

    def trigger_damage_dealt_to_other(self, unit, target, damage_before_mitigation, post_mitigation_damage, damage_type):
        if damage_type in ('magic', 'true'):
            unit.heal_with_overheal(0.40 * post_mitigation_damage, self.uuid, 300)
            heal_target = None
            for ally in unit.get_allies():
                if heal_target is None or ally.health / ally.total_health < heal_target.health / heal_target.total_health:
                    heal_target = ally
            if heal_target:
                heal_target.heal(0.40 * post_mitigation_damage)