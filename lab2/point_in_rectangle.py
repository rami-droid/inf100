def point_in_rectangle(x1, y1, x2, y2, px, py):
    right, left = max(x1, x2), min(x1, x2)
    up, down = max(y1, y2), min(y1, y2)

    return (py >= down and py <= up) and (px >= left and px <= right)


def test_point_in_rectangle():
    print("Tester point_in_rectangle... ", end="")
    assert point_in_rectangle(0, 0, 5, 5, 3, 3) is True  # Midt i
    assert point_in_rectangle(0, 5, 5, 0, 5, 3) is True  # På kanten
    assert point_in_rectangle(0, 0, 5, 5, 6, 3) is False  # Utenfor
    print("OK")


test_point_in_rectangle()
