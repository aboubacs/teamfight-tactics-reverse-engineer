from synergies.synergy import Synergy

class Knight(Synergy):
    steps = [2, 4, 6]

    def get_flat_damage_reduction(self):
        return {
            2: 20,
            4: 40,
            6: 70,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        unit.flat_damage_reduction_modifiers.add_component(self.uuid, 0, 9999, self.get_flat_damage_reduction())
