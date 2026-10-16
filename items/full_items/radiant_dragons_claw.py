from items.item import Item
from units.unit import Unit

class RadiantDragonsClaw(Item):
    def __init__(self):
        super().__init__('radiant_dragons_claw')
        self.last_fireball_at = -1
        self.fireball_cooldown = 1
        self.heal_last_triggered_at = 0

    def get_magic_resist_bonus(self):
        return 300

    def on_damage_taken(self, unit, damage_source, pre_mitigation_damage, post_mitigation_damage, damage_type):
        if not isinstance(damage_source, Unit):
            return
        if damage_type in ('magic', 'true') and unit._TIME >= self.last_fireball_at + self.fireball_cooldown:
            self.last_fireball_at = unit._TIME
            unit.deal_magic_damage(damage_source, 0.4 * damage_source.total_health, can_crit=False)

    def tick(self, unit, map, time):
        if time >= self.heal_last_triggered_at + 1:
            self.heal_last_triggered_at = time
            unit.heal(0.02 * unit.total_health)