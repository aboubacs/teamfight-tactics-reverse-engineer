from synergies.synergy import Synergy

class Nightbringer(Synergy):
    steps = [2, 4, 6, 8]

    def get_shield_ratio(self):
        return {
            2: 0.3,
            4: 0.6,
            6: 0.9,
            8: 2.0,
        }[self.activated_step]

    def get_damage_multiplier(self):
        return {
            2: 0.2,
            4: 0.3,
            6: 0.4,
            8: 0.7,
        }[self.activated_step]

    def on_start_fight(self, units):
        self.units_with_shield_activated = set()

    def tick(self, time, units):
        for unit in units:
            if self.__class__ in unit.synergies and unit.uuid not in self.units_with_shield_activated:
                if unit.health < unit.total_health * 0.5:
                    self.units_with_shield_activated.add(unit.uuid)
                    unit.add_shield_effect(unit.total_health * self.get_shield_ratio(), 8)
                    unit.innate_bonus_damage_multiplier_modifiers.add_component('nightbringer', time, 9999, self.get_damage_multiplier())
