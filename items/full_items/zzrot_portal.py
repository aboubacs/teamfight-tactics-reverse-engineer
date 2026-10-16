from items.item import Item
from units.set5.voidspawn import Voidspawn

class ZzrotPortal(Item):
    def __init__(self):
        super().__init__('zzrot_portal')
        self.has_ticked = False

    def get_attack_speed_bonus(self):
        return 0.10

    def trigger_on_add(self, map, unit):
        unit.increase_health(150)

    def trigger_on_death(self, unit):
        row, col = unit.closest_empty_tile(unit._MAP)
        unit._MAP.spawn_unit(Voidspawn(team=unit.team, row=row, col=col))

    def tick(self, unit, map, time):
        if not self.has_ticked:
            self.has_ticked = True

            for enemy in unit.targetable_enemies(map):
                if enemy.distance(unit.row, unit.col) <= 2:
                    enemy.current_target = unit