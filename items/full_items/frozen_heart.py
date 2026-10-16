from items.item import Item

class FrozenHeart(Item):
    def __init__(self):
        super().__init__('frozen_heart')

    def trigger_on_add(self, map, unit):
        unit.increase_mana(15)

    def get_armor_bonus(self):
        return 20

    def tick(self, unit, map, time):
        for u in map.units:
            if u.team != unit.team and u.distance(unit.row, unit.col) <= 2:
                u.attack_speed_multiplier_modifiers.add_component(self.uuid, time, 0.5, 0.75)