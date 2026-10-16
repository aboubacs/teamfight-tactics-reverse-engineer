from items.item import Item

class RadiantRedemption(Item):
    def __init__(self):
        super().__init__('radiant_redemption')
        self.last_tick_at = 0
        self.tick_period = 5
        self.range = 2
        self.heal_ratio_missing_health = 0.25

    def trigger_on_add(self, map, unit):
        unit.increase_health(150 + 350)
        unit.increase_mana(15)

    def tick(self, unit, map, time):
        if time >= self.last_tick_at + self.tick_period:
            self.last_tick_at = time
            for u in map.units:
                if u.team == unit.team and unit.distance(u.row, u.col) <= self.range:
                    u.heal((u.total_health - u.health) * self.heal_ratio_missing_health)
                    u.multitarget_percent_damage_reduction_modifiers.add_component(self.uuid, time, 5, 25)