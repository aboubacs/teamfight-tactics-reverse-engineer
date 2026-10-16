from items.item import Item

class StatikkShiv(Item):
    def __init__(self):
        super().__init__('statikk_shiv')
        self.aa_count = 0

    def get_attack_speed_bonus(self):
        return 0.10

    def trigger_on_add(self, map, unit):
        unit.increase_mana(15)

    def before_auto_attack(self, unit, target, map, time):
        self.aa_count += 1
        if self.aa_count % 3 == 0:
            enemies = [u for u in map.units if u.team != unit.team]
            sorted_enemies = sorted(
                enemies,
                key=lambda e: e.distance(target.row, target.col)
            )
            for lightning_target in sorted_enemies[:4]:
                lightning_target.magic_resist_shred_percentage_modifiers.add_component(self.uuid, time, 5, 0.5)
                unit.deal_magic_damage(lightning_target, 70, can_crit=False, can_remove_spell_shield=False)
