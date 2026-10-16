from synergies.synergy import Synergy

class Dawnbringer(Synergy):
    steps = [2, 4, 6, 8]

    def get_healing_ratio(self):
        return {
            2: 0.30,
            4: 0.55,
            6: 0.80,
            8: 1.20
        }[self.activated_step]

    def get_healing_ticks_count(self):
        return {
            2: 10,
            4: 15,
            6: 20,
            8: 25
        }[self.activated_step]

    def get_damage_multiplier_per_trigger(self):
        return 0.10

    def on_start_fight(self, units):
        self.ticks_per_second = 5
        self.units_info = {}

    def tick(self, time, units):
        for unit in units:
            if self.__class__ in unit.synergies:
                unit.innate_bonus_damage_multiplier_modifiers.add_component(
                    'dawnbringer', time, 9999,
                    self.get_damage_multiplier_per_trigger() * len([u for u in self.units_info.values() if u['triggered']])
                )

                if unit.uuid not in self.units_info:
                    self.units_info[unit.uuid] = {
                        'triggered': False,
                        'ticks_remaining': 0,
                        'next_tick_at': None
                    }
                if not self.units_info[unit.uuid]['triggered'] and unit.health < unit.total_health * 0.5:
                    self.units_info[unit.uuid]['triggered'] = True
                    self.units_info[unit.uuid]['ticks_remaining'] = self.get_healing_ticks_count()
                    self.units_info[unit.uuid]['next_tick_at'] = time

                if self.units_info[unit.uuid]['ticks_remaining'] and time >= self.units_info[unit.uuid]['next_tick_at']:
                    self.units_info[unit.uuid]['ticks_remaining'] -= 1
                    if self.units_info[unit.uuid]['ticks_remaining'] > 0:
                        self.units_info[unit.uuid]['next_tick_at'] += 1 / self.ticks_per_second
                    unit.heal(unit.total_health * self.get_healing_ratio() / self.get_healing_ticks_count())

