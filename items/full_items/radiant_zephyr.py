from items.item import Item

class RadiantZephyr(Item):
    def __init__(self):
        super().__init__('radiant_zephyr')
        self.zephyr_time = 10

    def get_magic_resist_bonus(self):
        return 20

    def trigger_on_add(self, map, unit):
        unit.increase_health(150)

        for u in map.units:
            if u.team == unit.team:
                u.base_attack_speed_bonus_ratio_modifiers.add_component(self.uuid, 0, 9999, 0.20)

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
