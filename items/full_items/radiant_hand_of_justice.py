import random

from items.item import Item

class RadiantHandOfJustice(Item):
    def __init__(self):
        super().__init__('radiant_hand_of_justice')
        self.mode_damage = random.random() >= 0.5

    def get_critical_chance_bonus(self):
        return 0.15

    def get_attack_damage_bonus(self):
        return 40

    def get_spell_power_bonus(self):
        return 40

    def trigger_on_add(self, map, unit):
        unit.increase_mana(15)

    def trigger_damage_dealt_to_other(self, unit, target, damage_before_mitigation, post_mitigation_damage, type):
        unit.heal(0.40 * post_mitigation_damage)