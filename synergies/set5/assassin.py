from synergies.synergy import Synergy

class Assassin(Synergy):
    steps = [2, 4, 6]

    def get_bonus_crit_chance(self):
        return {
            2: 0.10,
            4: 0.30,
            6: 0.50,
        }[self.activated_step]

    def get_bonus_crit_damage(self):
        return {
            2: 0.30,
            4: 0.50,
            6: 0.70,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.base_critical_chance += self.get_bonus_crit_chance()
            unit.flat_bonus_crit_damage += self.get_bonus_crit_damage()
