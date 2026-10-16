from items.item import Item
from dot import Dot

class MorellonomiconBurn(Dot):
    def is_burn_dot(self):
        return True

    def trigger(self, map, time):
        self.owner.deal_true_damage(
            self.unit,
            self.unit.total_health * 2.5 / 100,
            can_crit=False,
            can_remove_spell_shield=False
        )

class Morellonomicon(Item):
    def __init__(self):
        super().__init__('morellonomicon')

    def trigger_on_add(self, map, unit):
        unit.increase_health(150)

    def get_spell_power_bonus(self):
        return 10

    def trigger_damage_dealt_to_other(self, unit, target, damage_before_mitigation, post_mitigation_damage, damage_type):
        if damage_type in ('magic', 'true'):
            target.apply_hemoragy(unit._TIME, 10)
            if any(dot.is_burn_dot() for dot in target.dots):
                return
            target.dots.append(
                MorellonomiconBurn(
                    owner=unit,
                    unit=target,
                    time=unit._TIME,
                    trigger_delay=1,
                    trigger_duration=10,
                )
            )
