from dataclasses import dataclass

@dataclass
class Shield:
    value: int
    expires_at: int
    identifier: str

    def absorb_and_return_remaining_damage(self, damage):
        if damage >= self.value:
            self.value = 0
            return damage - self.value
        else:
            self.value -= damage
            return 0

class ShieldManager():

    def __init__(self):
        self.shields = []

    def get_total_shield_value(self):
        if not self.shields:
            return 0
        return sum([s.value for s in self.shields])

    def has_shield(self, identifier):
        return len([s for s in self.shields if s.identifier == identifier]) > 0

    def get_shield(self, identifier):
        if not self.has_shield(identifier):
            return None
        return [s for s in self.shields if s.identifier == identifier][0]

    def add_shield_effect(self, current_time, shield_value, shield_duration, shield_identifier=""):
        self.shields.append(Shield(value=shield_value, expires_at=current_time + shield_duration, identifier=shield_identifier))

    def absorb_and_return_remaining_damage(self, damage):
        while self.shields and damage:
            best_shield = self.get_fastest_expiring_shield()
            damage = best_shield.absorb_and_return_remaining_damage(damage)
            self.shields = [shield for shield in self.shields if shield.value > 0]
            return self.absorb_and_return_remaining_damage(damage)
        return damage

    def get_fastest_expiring_shield(self):
        return sorted(self.shields, key=lambda s: s.expires_at)[0]

    def update_shields(self, current_time):
        self.shields = [shield for shield in self.shields if shield.expires_at > current_time]