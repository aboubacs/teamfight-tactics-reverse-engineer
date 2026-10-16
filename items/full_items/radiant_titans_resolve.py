from items.item import Item

class RadiantTitansResolve(Item):
    def __init__(self):
        super().__init__('radiant_titans_resolve')
        self.stacks = 0
        self.ad_per_stack = 6
        self.ap_per_stack = 6

    def get_attack_speed_bonus(self):
        return 0.10

    def get_armor_bonus(self):
        return 20 + (50 if self.stacks >= 25 else 0)

    def get_magic_resist_bonus(self):
        return 50 if self.stacks >= 25 else 0

    def get_attack_damage_bonus(self):
        return self.ad_per_stack * self.stacks

    def get_spell_power_bonus(self):
        return self.ap_per_stack * self.stacks

    def on_damage_taken(self, unit, damage_source, pre_mitigation_damage, post_mitigation_damage, damage_type):
        if self.stacks < 25:
            self.stacks += 1

    def before_auto_attack(self, unit, target, map, time):
        if self.stacks < 25:
            self.stacks += 1