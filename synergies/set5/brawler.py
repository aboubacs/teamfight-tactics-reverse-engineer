from synergies.synergy import Synergy

class Brawler(Synergy):
    steps = [2, 4, 6]

    def get_bonus_health(self):
        return {
            2: 400,
            4: 1000,
            6: 1600,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.increase_health(self.get_bonus_health())