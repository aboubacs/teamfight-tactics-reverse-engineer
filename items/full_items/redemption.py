from items.item import Item

class Redemption(Item):
    def __init__(self):
        super().__init__('redemption')
        self.last_tick_at = 0
        self.tick_period = 5
        self.range = 1
        self.heal_ratio_missing_health = 0.18

    def trigger_on_add(self, map, unit):
        unit.increase_health(150)
        unit.increase_mana(15)

    def tick(self, unit, map, time):
        if time >= self.last_tick_at + self.tick_period:
            self.last_tick_at = time
            for u in map.units:
                if u.team == unit.team and unit.distance(u.row, u.col) <= self.range:
                    u.heal((u.total_health - u.health) * self.heal_ratio_missing_health)
                    u.multitarget_percent_damage_reduction_modifiers.add_component(self.uuid, time, 5, 25)