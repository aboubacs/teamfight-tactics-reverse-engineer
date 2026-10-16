from items.item import Item

class GuardianAngel(Item):
    def __init__(self):
        super().__init__('guardian_angel')

    def get_attack_damage_bonus(self):
        return 10

    def get_armor_bonus(self):
        return 20

    def trigger_on_add(self, map, unit):
        unit.revive_with += 400