from items.item import Item

class RadiantGuardianAngel(Item):
    def __init__(self):
        super().__init__('radiant_guardian_angel')

    def get_attack_damage_bonus(self):
        return 10

    def get_armor_bonus(self):
        return 20

    def get_attack_speed_bonus(self):
        return 0.30

    def trigger_on_add(self, map, unit):
        unit.revive_with = unit.total_health