class Dot:
    def __init__(self, owner, unit, time, trigger_delay, trigger_duration):
        self.start_time = time
        self.next_tick_at = self.start_time
        self.trigger_delay = trigger_delay
        self.trigger_duration = trigger_duration
        self.owner = owner
        self.unit = unit
        self.destroyed = False

    def update_state(self, time):
        self.destroyed = time > self.start_time + self.trigger_duration

    def refresh(self, time):
        self.start_time = time

    def tick(self, map, time):
        if self.destroyed:
            return
        if time >= self.next_tick_at:
            self.next_tick_at = time + self.trigger_delay
            self.trigger(map, time)

    def trigger(self, map, time):
        pass

    def is_burn_dot(self):
        return False