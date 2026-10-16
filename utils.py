def xy_pos_from_ij_tile(i, j):
    return (70*j + (35 if i % 2 else 0), 60*i)

def rc_from_xy(x, y):
    row = y // 60
    if row < 0: row = 0
    if row > 7: row = 7
    if row % 2:
        x -= 35
    col = x // 70
    if col < 0: col = 0
    if col > 6: col = 6
    return (row, col)

def axial_to_cube(r, c):
    if r <= 1:
        c += 1
    if r <= 3:
        c += 1
    if r <= 5:
        c += 1
    x = c
    z = r
    y = -x-z
    return (x, y, z)

def distance(r1, c1, r2, c2):
    x1, y1, z1 = axial_to_cube(r1, c1)
    x2, y2, z2 = axial_to_cube(r2, c2)
    return (abs(x2-x1) + abs(y2-y1) + abs(z2-z1))//2

def xydistance2(r1, c1, r2, c2):
    x1, y1 = xy_pos_from_ij_tile(r1, c1)
    x2, y2 = xy_pos_from_ij_tile(r2, c2)
    return (x2-x1)**2 + (y2-y1)**2

def get_neighbours(row, col):
    neighbours = []
    if col > 0:
        neighbours.append((row, col-1))
    if col < 6:
        neighbours.append((row, col+1))
    if row % 2:
        neighbours.append((row-1, col))
        if col < 6:
            neighbours.append((row-1, col+1))
        if row < 7:
            neighbours.append((row+1, col))
            if col < 6:
                neighbours.append((row+1, col+1))
    else:
        neighbours.append((row+1, col))
        if col > 0:
            neighbours.append((row+1, col-1))
        if row > 0:
            neighbours.append((row-1, col))
            if col > 0:
                neighbours.append((row-1, col-1))
    return neighbours


def closest_empty_tile_from_pos(base_row, base_col, map, farthest_from_row=None, farthest_from_col=None, closest_from_row=None, closest_from_col=None):
    best_tile = None
    for row in range(8):
        for col in range(7):
            if not map.is_tile_empty(row, col):
                continue
            if best_tile is None:
                best_tile = (row, col)
                continue
            if xydistance2(base_row, base_col, row, col) < xydistance2(base_row, base_col, best_tile[0], best_tile[1]):
                best_tile = (row, col)
            elif xydistance2(base_row, base_col, row, col) == xydistance2(base_row, base_col, best_tile[0], best_tile[1]) and farthest_from_col and farthest_from_row:
                if xydistance2(farthest_from_row, farthest_from_col, row, col) > xydistance2(farthest_from_row, farthest_from_col, best_tile[0], best_tile[1]):
                    best_tile = (row, col)
            elif xydistance2(base_row, base_col, row, col) == xydistance2(base_row, base_col, best_tile[0], best_tile[1]) and closest_from_col and closest_from_row:
                if xydistance2(closest_from_row, closest_from_col, row, col) < xydistance2(closest_from_row, closest_from_col, best_tile[0], best_tile[1]):
                    best_tile = (row, col)
    return best_tile
