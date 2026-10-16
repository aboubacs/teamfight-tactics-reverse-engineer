from synergies.synergy import Synergy

class Cavalier(Synergy):
    steps = [2, 3, 4]

    def get_percent_damage_reduction(self):
        return {
            2: 20,
            3: 25,
            4: 30,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.percent_damage_reduction_modifiers.add_component('cavalier_background', 0, 9999, self.get_percent_damage_reduction())
            unit.percent_damage_reduction_modifiers.add_component('cavalier_charge', 0, 4, self.get_percent_damage_reduction())
