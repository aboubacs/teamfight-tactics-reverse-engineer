import uuid
from synergies.synergy import Synergy

class Skirmisher(Synergy):
    steps = [3, 6, 9]

    def get_bonus_shield_hp_ratio(self):
        return {
            3: 0.20,
            6: 0.40,
            9: 1.00
        }[self.activated_step]

    def get_bonus_ad(self):
        return {
            3: 3,
            6: 6,
            9: 15
        }[self.activated_step]

    def on_start_fight(self, units):
        self.last_tick_at = 0

    def apply_on_unit_spawn(self, unit):
        if self.__class__ in unit.synergies:
            unit.add_shield_effect(self.get_bonus_shield_hp_ratio() * unit.total_health, 9999)

    def tick(self, time, units):
        if time >= self.last_tick_at + 1:
            self.last_tick_at = time
            for unit in units:
                if self.__class__ in unit.synergies:
                    unit.flat_bonus_attack_damage_modifiers.add_component(uuid.uuid4(), time, 9999, self.get_bonus_ad())