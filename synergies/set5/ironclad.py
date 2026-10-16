from synergies.synergy import Synergy

class Ironclad(Synergy):
    steps = [2, 3, 4]

    def get_bonus_armor(self):
        return {
            2: 30,
            3: 70,
            4: 125,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        unit.flat_bonus_armor_modifiers.add_component(self.uuid, 0, 9999, self.get_bonus_armor())
