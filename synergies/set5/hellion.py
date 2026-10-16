from synergies.synergy import Synergy

class Hellion(Synergy):
    steps = [2, 4, 6, 8]

    def get_bonus_as(self):
        return {
            2: 0.10,
            4: 0.30,
            6: 0.70,
            8: 1.30,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.base_attack_speed_bonus_ratio_modifiers.add_component(self.uuid, 0, 9999, self.get_bonus_as())
            unit.should_spawn_hellion = True
