def find_treasure(grid, target_sum):
    treasures = []
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            curr = grid[col][row] + col + row
            if curr == target_sum:
                treasures.append([col, row])
    return treasures


def test_find_treasure():
    print("Testing find_treasure... ", end="")
    # Test 1
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    target_value = 5
    actual = find_treasure(grid, target_value)
    expected = [[0, 2], [1, 0]]
    assert expected == actual

    # Test 2
    actual = find_treasure([[1, 2], [3, 4]], 3)
    expected = [[0, 1]]
    assert expected == actual

    # Test 3
    actual = find_treasure([[1, 2], [3, 4]], 1)
    expected = [[0, 0]]
    assert expected == actual

    # Test 4
    actual = find_treasure([[1, 2], [3, 4]], 1000)
    expected = []
    assert expected == actual

    print("OK")


test_find_treasure()
