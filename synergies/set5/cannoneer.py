from synergies.synergy import Synergy

class Cannoneer(Synergy):
    steps = [2, 4, 6]

    def get_ad_ratio_damage(self):
        return {
            2: 2.25,
            4: 4.5,
            6: 12,
        }[self.activated_step]

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.cannoneer_active = True
            unit.cannoneer_ad_ratio = self.get_ad_ratio_damage()
