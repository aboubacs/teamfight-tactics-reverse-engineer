from items.item import Item

class ArchangelsStaff(Item):
    def __init__(self):
        super().__init__('archangels_staff')
        self.bonus_ap = 0

    def get_spell_power_bonus(self):
        return 10 + self.bonus_ap

    def trigger_on_add(self, map, unit):
        unit.increase_mana(15)

    def on_spell_cast(self, unit):
        self.bonus_ap += 0.40 * unit.get_effective_total_mana()