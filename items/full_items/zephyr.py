from items.item import Item

class Zephyr(Item):
    def __init__(self):
        super().__init__('zephyr')
        self.zephyr_time = 5

    def get_magic_resist_bonus(self):
        return 20

    def trigger_on_add(self, map, unit):
        unit.increase_health(150)

        opposite_pos = (7 - unit.row, 6 - unit.col)
        enemies = [u for u in map.units if u.team != unit.team]
        sorted_enemies = sorted(
            enemies,
            key=lambda e: e.distance(opposite_pos[0], opposite_pos[1])
        )
        if not sorted_enemies:
            return

        target = sorted_enemies[0]
        target.is_under_zephyr = True
        target.under_zephyr_until = self.zephyr_time
        target.is_targetable = False
        target.untargetable_until = self.zephyr_time
