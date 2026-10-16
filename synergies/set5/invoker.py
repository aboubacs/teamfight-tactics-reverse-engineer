from synergies.synergy import Synergy

class Invoker(Synergy):
    steps = [2, 4]

    def get_bonus_mana_on_attack(self):
        return {
            2: 3,
            4: 6,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        unit.mana_per_auto += self.get_bonus_mana_on_attack()