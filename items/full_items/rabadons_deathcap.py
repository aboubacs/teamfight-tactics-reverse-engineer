from items.item import Item

class RadabonsDeathcap(Item):
    def __init__(self):
        super().__init__('rabadons_deathcap')

    def get_spell_power_bonus(self):
        return 75