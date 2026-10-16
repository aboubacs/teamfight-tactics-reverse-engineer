from synergies.synergy import Synergy

class Mystic(Synergy):
    steps = [2, 3, 4, 5]

    def get_bonus_magic_resist(self):
        return {
            2: 40,
            3: 80,
            4: 150,
            5: 250,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        unit.flat_bonus_magic_resist_modifiers.add_component(self.uuid, 0, 9999, self.get_bonus_magic_resist())
