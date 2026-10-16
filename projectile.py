import math
import pygame
import utils

UNIT_RADIUS = 30

class Projectile:
    XY_OFFSET = 40
    HEX_TO_XY_DISTANCE_RATIO = 65

    def __init__(self, map, owner, time, x0, y0, xE, yE, radius, hex_per_second):
        self.map = map
        self.owner = owner
        self.start_time = time
        self.x0 = x0 + self.XY_OFFSET
        self.y0 = y0 + self.XY_OFFSET
        self.xE = xE + self.XY_OFFSET
        self.yE = yE + self.XY_OFFSET
        self.radius = radius
        self.travel_distance = math.sqrt((xE-x0)**2 + (yE-y0)**2)
        self.hex_per_second = hex_per_second
        self.travel_time = self.travel_distance / (hex_per_second * self.HEX_TO_XY_DISTANCE_RATIO)
        self.destroyed = False
        self.unit_uuids_hit = set()

    def to_log_json(self, time):
        x, y = self.get_xy_pos(time)
        return {
            'x': x,
            'y': y,
            'radius': self.radius
        }

    def update_state(self, time):
        self.destroyed = time > self.start_time + self.travel_time

    def get_xy_pos(self, time):
        travel_ratio = (time - self.start_time) / self.travel_time if self.travel_time else 0
        if travel_ratio == 0:
            return (self.x0, self.y0)
        return (
            self.x0 + (self.xE-self.x0)*travel_ratio,
            self.y0 + (self.yE-self.y0)*travel_ratio
        )

    def draw(self, screen, time):
        base_tile_pos = self.get_xy_pos(time)
        pygame.draw.circle(screen, (255, 0, 0), (base_tile_pos[0], base_tile_pos[1]), self.radius)

    def tick(self, time):
        self.update_state(time)
        x, y = self.get_xy_pos(time)
        for unit in self.map.units:
            if self.destroyed:
                break
            if unit.uuid in self.unit_uuids_hit:
                continue
            xu, yu = utils.xy_pos_from_ij_tile(unit.row, unit.col)
            xu += UNIT_RADIUS
            yu += UNIT_RADIUS
            d = math.sqrt((x-xu)**2 + (y-yu)**2)
            if d < UNIT_RADIUS + self.radius:
                self.unit_uuids_hit.add(unit.uuid)
                self.on_unit_hit(time, unit)

    def on_unit_hit(self, time, unit):
        pass

    def on_destroy(self, map, time):
        pass