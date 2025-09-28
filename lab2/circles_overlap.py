def circles_overlap(x1, y1, r1, x2, y2, r2):
    dx = x2 - x1
    dy = y2 - y1

    distance_squared = dx * dx + dy * dy
    radius_sum = r1 + r2
    return distance_squared <= radius_sum * radius_sum
