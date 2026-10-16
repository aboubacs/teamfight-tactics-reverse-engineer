import utils

from items.item import Item
from aoe import AOE

class RadiantShroudOfStillness(Item):
    def __init__(self):
        super().__init__('radiant_shroud_of_stillness')
        self.has_ticked = False
        self.radius = 150

    def get_armor_bonus(self):
        return 20

    def get_dodge_bonus(self):
        return 0.15

    def tick(self, unit, map, time):
        if not self.has_ticked:
            self.has_ticked = True

            x, y = utils.xy_pos_from_ij_tile(unit.row, unit.col)
            aoe = AOE([
                (x - self.radius, y - 9999),
                (x + self.radius, y - 9999),
                (x + self.radius, y + 9999),
                (x - self.radius, y + 9999)
            ])
            for u in map.units:
                if u.team != unit.team and aoe.is_unit_inside(u):
                    u.shroud(50)
                elif u.team == unit.team:
                    u.increase_mana(15)