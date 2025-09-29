def smallest_absolute_difference(a):
    smallest = float("inf")
    # a = list(map(abs, a))
    new_nums = []
    for num in a:
        new_nums.append(num)
        new_nums.sort()
    for i in range(len(new_nums) - 1):
        if abs(new_nums[i + 1] - new_nums[i]) < smallest:
            smallest = new_nums[i + 1] - new_nums[i]
    return smallest


def test_smallest_absolute_difference():
    print("Tester smallest_absolute_difference... ", end="")
    assert 1 == smallest_absolute_difference([1, 20, 4, 19, -5, 99])  # 20-19
    assert 6 == smallest_absolute_difference([67, 19, 40, -5, 1])  # 1-(-5)
    assert 0 == smallest_absolute_difference([2, 1, 4, 1, 5, 6])  # 1-1
    a = [50, 40, 70, 33]
    assert 7 == smallest_absolute_difference(a)
    assert [50, 40, 70, 33] == a  # Sjekker at funksjonen ikke er destruktiv
    print("OK")


test_smallest_absolute_difference()
