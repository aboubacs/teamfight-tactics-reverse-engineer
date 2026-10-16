from items.item import Item

class RadiantLastWhisper(Item):
    def __init__(self):
        super().__init__('radiant_last_whisper')

    def get_critical_chance_bonus(self):
        return 0.15 + 0.35

    def get_attack_speed_bonus(self):
        return 0.10

    def on_crit(self, unit, target):
        target.armor_shred_percentage_modifiers.add_component(self.uuid, unit._TIME, 9999, 0.7)