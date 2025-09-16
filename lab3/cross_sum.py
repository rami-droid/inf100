# def cross_sum(x):
#    x = str(x)
#    digits = []
#    sum = 0
#
#    for digit in x:
#        digits.append(int(digit))
#    for digit in digits:
#        sum += digit
#    return sum


def cross_sum(n):
    return sum(int(d) for d in str(n))


def nth_cross_sum(n, x):
    count = 0
    num = 0
    while True:
        if cross_sum(num) == x:
            count += 1
            if count == n:
                return num
        num += 1


# def nth_cross_sum(x, n):
#     count = 0
#
#     while count < n:
#         if cross_sum(n) == x:
#             count += 1
#     return count


def test_cross_sum():
    print("Tester cross_sum... ", end="")
    assert 6 == cross_sum(123)
    assert 7 == cross_sum(34)
    assert 0 == cross_sum(0)
    assert 1 == cross_sum(100)
    print("OK")


def test_nth_cross_sum():
    print("Tester nth_cross_sum... ", end="")
    assert nth_cross_sum(3, 7) == 25
    assert nth_cross_sum(1, 10) == 19
    assert nth_cross_sum(2, 10) == 28
    assert nth_cross_sum(10, 2) == 2000
    print("OK")


test_nth_cross_sum()
