import uuid

from synergies.synergy import Synergy

class Sentinel(Synergy):
    steps = [3, 6, 9]

    def get_expire_duration(self):
        return {
            3: 4,
            6: 2,
            9: 1,
        }[self.activated_step]

    def get_shield_value(self):
        return {
            3: 200,
            6: 1000,
            9: 2000,
        }[self.activated_step]

    def get_bonus_as(self):
        return {
            3: 0.25,
            6: 1.2,
            9: 10
        }[self.activated_step]

    def apply_bonus_on(self, unit, time):
        self.next_expire_at = time + self.get_expire_duration()
        unit.add_shield_effect(self.get_shield_value(), self.get_expire_duration(), identifier='sentinel')
        unit.base_attack_speed_bonus_ratio_modifiers.add_component(uuid.uuid4(), time, 9999, self.get_bonus_as())
        self.current_unit_with_bonus = unit

    def on_start_fight(self, units):
        self.next_expire_at = self.get_expire_duration()
        self.apply_bonus_on(
            sorted(
                [u for u in units if self.__class__ in u.synergies],
                key=lambda u: u.total_health,
                reverse=True
            )[0],
            0
        )

    def tick(self, time, units):
        if not units:
            return
        if time >= self.next_expire_at or not self.current_unit_with_bonus.shield_manager.has_shield('sentinel'):
            candidates = [u for u in units if u != self.current_unit_with_bonus]
            if candidates:
                self.apply_bonus_on(sorted(candidates, key=lambda u: u.health/u.total_health)[0], time)