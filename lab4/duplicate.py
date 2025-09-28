def duplicate(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return


def duplicated(numbers):
    return list(map(lambda x: x * 2, numbers))


def duplicate_2d(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col] *= 2
    return


def duplicated_2d(grid):
    new_grid = []
    for row in range(len(grid)):
        new_grid.append(list(map(lambda x: x * 2, grid[row])))
    return new_grid


def test_duplicated_2d():
    print("Testing duplicated_2d...", end=" ", flush=True)

    # Test 1
    arg = [[2, 3, 4], [4, 1, 0]]
    return_val = duplicated_2d(arg)
    expected = [[4, 6, 8], [8, 2, 0]]
    assert return_val == expected
    assert arg == [[2, 3, 4], [4, 1, 0]]

    # Test 2
    arg = [[3, 2], [2, 1], [1, 0]]
    return_val = duplicated_2d(duplicated_2d(arg))
    expected = [[12, 8], [8, 4], [4, 0]]
    assert return_val == expected
    assert arg == [[3, 2], [2, 1], [1, 0]]

    print("OK")


def test_duplicate_2d():
    print("Testing duplicate_2d...", end=" ", flush=True)

    # Test 1
    arg = [[2, 3, 4], [4, 1, 0]]
    return_val = duplicate_2d(arg)
    expected = [[4, 6, 8], [8, 2, 0]]
    assert return_val is None
    assert expected == arg

    # Test 2
    arg = [[3, 2], [2, 1], [1, 0]]
    duplicate_2d(arg)
    duplicate_2d(arg)
    expected = [[12, 8], [8, 4], [4, 0]]
    assert expected == arg

    print("OK")


test_duplicated_2d()


def test_duplicate():
    print("Testing duplicate...", end=" ", flush=True)

    # Test 1
    arg = [2, 3, 10, 3, 4]
    return_val = duplicate(arg)
    expected = [4, 6, 20, 6, 8]
    assert return_val is None
    assert expected == arg

    # Test 2
    arg = [3, 2]
    duplicate(arg)
    duplicate(arg)
    expected = [12, 8]
    assert expected == arg

    print("OK")


def test_duplicated():
    print("Testing duplicated...", end=" ", flush=True)

    # Test 1
    arg = [2, 3, 10, 3, 4]
    return_val = duplicated(arg)
    expected = [4, 6, 20, 6, 8]
    assert return_val == expected
    assert arg == [2, 3, 10, 3, 4]

    # Test 2
    arg = [3, 2]
    return_val = duplicated(duplicated(arg))
    expected = [12, 8]
    assert return_val == expected
    assert arg == [3, 2]

    print("OK")
