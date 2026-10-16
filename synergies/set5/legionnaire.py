from synergies.synergy import Synergy

class Legionnaire(Synergy):
    steps = [2, 4, 6, 8]

    def get_bonus_as(self):
        return {
            2: 0.25,
            4: 0.65,
            6: 1.20,
            8: 2.50,
        }[self.activated_step]

    def get_omnivamp_ratio(self):
        return {
            2: 0.15,
            4: 0.20,
            6: 0.25,
            8: 0.35,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.base_attack_speed_bonus_ratio_modifiers.add_component(self.uuid, 0, 9999, self.get_bonus_as())
            unit.legionnaire_omnivamp_ratio = self.get_omnivamp_ratio()
