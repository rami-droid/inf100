def largest_factor_of(x):
    for i in range(x - 1, 0, -1):
        if x % i == 0:
            return i
    # n1, n2 = 1, 1
    # largest = 0
    #     while True:
    #         while n1 * n2 < x:
    #             n1 += 1
    #             if n1 * n2 == x:
    #                 largest = max(n1, n2)
    #                 if largest == x:
    #                     largest = 0
    #                 else:
    #                     return largest
    #         n1 = 1
    #         n2 += 1


def test_largest_factor_of():
    print("Testing largest_factor_of... ", end="")
    assert 3 == largest_factor_of(6)
    assert 1 == largest_factor_of(7)
    assert 4 == largest_factor_of(8)
    print("OK")


test_largest_factor_of()
