from items.item import Item

class RadiantBansheesClaw(Item):
    def __init__(self):
        super().__init__('radiant_banshees_claw')

    def get_dodge_bonus(self):
        return 0.15

    def trigger_on_add(self, map, unit):
        unit.increase_health(150)
        for u in map.units:
            if u.team == unit.team:
                u.has_spell_shield = True
                u.increase_health(50)