from synergies.synergy import Synergy

class Redeemed(Synergy):
    steps = [3, 6, 9]

    def get_base_resist_stats(self):
        return {
            3: 20,
            6: 35,
            9: 75,
        }[self.activated_step]

    def get_base_ap_stats(self):
        return {
            3: 30,
            6: 60,
            9: 100,
        }[self.activated_step]

    def on_start_fight(self, units):
        self.init_nb_units_with_synergy = len([u for u in units if self.__class__ in u.synergies])

    def tick(self, time, units):
        nb_units_with_synergy = len([u for u in units if self.__class__ in u.synergies])
        if nb_units_with_synergy == 0:
            return
        nb_units_with_synergy_dead = self.init_nb_units_with_synergy - nb_units_with_synergy
        bonus_resist_stats = self.get_base_resist_stats() + nb_units_with_synergy_dead * (self.get_base_resist_stats() / nb_units_with_synergy)
        bonus_ap_stats = self.get_base_ap_stats() + nb_units_with_synergy_dead * (self.get_base_ap_stats() / nb_units_with_synergy)
        for unit in units:
            if self.__class__ in unit.synergies:
                unit.flat_bonus_spell_power_modifiers.add_component('redeemed', time, 9999, bonus_ap_stats)
                unit.flat_bonus_armor_modifiers.add_component('redeemed', time, 9999, bonus_resist_stats)
                unit.flat_bonus_magic_resist_modifiers.add_component('redeemed', time, 9999, bonus_resist_stats)