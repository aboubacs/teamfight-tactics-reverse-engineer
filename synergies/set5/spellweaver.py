from synergies.synergy import Synergy

class Spellweaver(Synergy):
    steps = [2, 4, 6]

    def get_base_bonus_ap(self):
        return {
            2: 25,
            4: 55,
            6: 100,
        }[self.activated_step]

    def get_bonus_ap_per_stack(self):
        return {
            2: 2,
            4: 5,
            6: 10,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.flat_bonus_spell_power_modifiers.add_component('spellweaver', 0, 9999, self.get_base_bonus_ap())
            unit.spellweaver_ap_gain_per_cast = self.get_bonus_ap_per_stack()
