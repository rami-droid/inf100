def rectangles_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    left1, right1 = min(x1, x2), max(x1, x2)
    up1, down1 = min(y1, y2), max(y1, y2)
    left2, right2 = min(x3, x4), max(x3, x4)
    up2, down2 = min(y3, y4), max(y3, y4)

    return not (right1 < left2 or right2 < left1 or down1 < up2 or down2 < up1)


def circle_overlaps_rectangle(x1, y1, x2, y2, xc, yc, rc):
    left1, right1 = min(x1, x2), max(x1, x2)
    up1, down1 = min(y1, y2), max(y1, y2)
    pass


# return left_a <= right_b and bottom_a <= bottom_b and right_b <= y4 and y3 <= y2


def test_rectangles_overlap():
    print("Tester rectangles_overlap... ", end="")
    assert rectangles_overlap(0, 0, 5, 5, 2, 2, 6, 6) is True  # Delvis overlapp
    assert rectangles_overlap(0, 5, 5, 0, 1, 1, 4, 4) is True  # Fullstendig overlapp
    assert rectangles_overlap(0, 1, 7, 2, 1, 0, 2, 7) is True  # Kryssende rektangler
    assert rectangles_overlap(0, 5, 5, 0, 5, 5, 7, 7) is True  # Deler et hjørne
    assert rectangles_overlap(0, 0, 5, 5, 3, 6, 5, 8) is False  # Utenfor
    print("OK")


test_rectangles_overlap()
