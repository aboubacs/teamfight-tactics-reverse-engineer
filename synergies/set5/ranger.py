import uuid
from synergies.synergy import Synergy

class Ranger(Synergy):
    steps = [2, 4, 6]

    def get_bonus_as(self):
        return {
            2: 0.80,
            4: 1.80,
            6: 4,
        }[self.activated_step]

    def on_start_fight(self, units):
        self.last_activated_at = -4

    def tick(self, time, units):
        if time >= self.last_activated_at + 8:
            self.last_activated_at = time
            for unit in units:
                if self.__class__ in unit.synergies:
                    unit.base_attack_speed_bonus_ratio_modifiers.add_component(uuid.uuid4(), time, 4, self.get_bonus_as())