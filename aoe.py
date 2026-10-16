import utils

UNIT_RADIUS = 30

class AOE:
    XY_OFFSET = 40

    def __init__(self, vertices):
        self.vertices = [
            (v[0] + self.XY_OFFSET, v[1] + self.XY_OFFSET)
            for v in vertices
        ]

    def is_on_right_side(self, x, y, xy0, xy1):
        x0, y0 = xy0
        x1, y1 = xy1
        a = float(y1 - y0)
        b = float(x0 - x1)
        c = - a*x0 - b*y0
        return a*x + b*y + c >= 0

    def is_xy_inside(self, x, y):
        num_vert = len(self.vertices)
        is_right = [self.is_on_right_side(x, y, self.vertices[i], self.vertices[(i + 1) % num_vert]) for i in range(num_vert)]
        all_left = not any(is_right)
        all_right = all(is_right)
        return all_left or all_right

    def is_unit_inside(self, unit):
        x, y = utils.xy_pos_from_ij_tile(unit.row, unit.col)
        x += UNIT_RADIUS
        y += UNIT_RADIUS
        return self.is_xy_inside(x, y)