class Modifier:
    def __init__(self, unit):
        self.components = {}
        unit.register_modifier(self)

    def get_component(self, key):
        return self.components.get(key)

    def reset(self):
        self.components = {}

    def add_component(self, key, current_time, duration, value, keep_highest_value=False):
        if key not in self.components:
            self.components[key] = (-1, 0)  # todo check bugs if we insert negative with keep highest
        if not keep_highest_value and current_time + duration > self.components[key][0]:
            self.components[key] = (current_time + duration, value)
        elif keep_highest_value and value > self.components[key][1]:
            self.components[key] = (current_time + duration, value)

    def update_components(self, current_time):
        self.components = {
            key: value
            for key, value in self.components.items()
            if value[0] >= current_time
        }

    def values(self):
        return [c[1] for c in self.components.values()]

    def max(self):
        if self.components:
            return max(self.values())

    def min(self):
        if self.components:
            return min(self.values())

    def sum(self):
        return sum(self.values())