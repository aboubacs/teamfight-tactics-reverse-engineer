import uuid

class Synergy:
    steps = []

    def __init__(self, activated_step):
        self.activated_step = activated_step
        self.uuid = uuid.uuid4()

    @classmethod
    def is_active(cls, units):
        nb_units_with_synergy = len(set([u.image_name for u in units if cls in u.synergies]))
        return nb_units_with_synergy >= cls.steps[0]

    @classmethod
    def get_active_step(cls, units):
        nb_units_with_synergy = len(set([u.image_name for u in units if cls in u.synergies]))
        for step in cls.steps[::-1]:
            if nb_units_with_synergy >= step:
                return step

    def apply_on_unit_spawn(self, unit):
        pass

    def on_start_fight(self, units):
        pass

    def tick(self, time, units):
        pass

    def on_death(self, board, time, death_count):
        pass