from items.item import Item
from units.unit import Unit

class DragonsClaw(Item):
    def __init__(self):
        super().__init__('dragons_claw')
        self.last_fireball_at = -1
        self.fireball_cooldown = 1

    def get_magic_resist_bonus(self):
        return 200

    def on_damage_taken(self, unit, damage_source, pre_mitigation_damage, post_mitigation_damage, damage_type):
        if not isinstance(damage_source, Unit):
            return
        if damage_type in ('magic', 'true') and unit._TIME >= self.last_fireball_at + self.fireball_cooldown:
            self.last_fireball_at = unit._TIME
            unit.deal_magic_damage(damage_source, 0.3 * damage_source.total_health, can_crit=False)