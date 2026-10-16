from synergies.synergy import Synergy

class Revenant(Synergy):
    steps = [2, 3, 4, 5]

    def get_revive_health_ratio(self):
        return {
            2: 0.10,
            3: 0.25,
            4: 0.45,
            5: 0.70,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.revive_with += unit.total_health * self.get_revive_health_ratio()
            unit.has_revenant = True
