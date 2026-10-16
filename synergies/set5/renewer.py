from synergies.synergy import Synergy

class Renewer(Synergy):
    steps = [2, 4, 6]

    def get_regen_ratio(self):
        return {
            2: 0.04,
            4: 0.07,
            6: 0.10,
        }[self.activated_step]

    def on_start_fight(self, units):
        self.last_ticked_at = 0

    def tick(self, time, units):
        if time >= self.last_ticked_at + 1:
            self.last_ticked_at = time
            for unit in units:
                if self.__class__ in unit.synergies:
                    if unit.health < unit.total_health:
                        unit.heal(self.get_regen_ratio() * unit.total_health)
                    else:
                        unit.increase_mana(self.get_regen_ratio() * unit.get_effective_total_mana())
