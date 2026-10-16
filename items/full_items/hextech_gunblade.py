import pygame
import uuid 

from items.item import Item

class HextechGunblade(Item):
    def __init__(self):
        super().__init__('hextech_gunblade')
        self.uuid = uuid.uuid4()

    def get_spell_power_bonus(self):
        return 10

    def get_attack_damage_bonus(self):
        return 10

    def trigger_damage_dealt_to_other(self, unit, target, damage_before_mitigation, post_mitigation_damage, damage_type):
        if damage_type in ('magic', 'true'):
            unit.heal_with_overheal(0.33 * post_mitigation_damage, self.uuid, 300)