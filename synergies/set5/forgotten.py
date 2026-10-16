
from synergies.synergy import Synergy

class Forgotten(Synergy):
    steps = [2, 4, 6, 8]

    def get_bonus_ad(self):
        return {
            2: 20,
            4: 40,
            6: 70,
            8: 200,
        }[self.activated_step]

    def get_bonus_ap(self):
        return {
            2: 20,
            4: 40,
            6: 70,
            8: 200,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.flat_bonus_attack_damage_modifiers.add_component(self.uuid, 0, 9999, self.get_bonus_ad() * (1 + 0.1 * unit.forgotten_stacks))
            unit.spell_power += self.get_bonus_ap() * (1 + 0.1 * unit.forgotten_stacks)
