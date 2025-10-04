def g(x):
    return (1 / 8) * (x**2) - (2 * x) + 10


def approx_area_under_g(x_lo, x_hi):
    return sum([g(x) for x in range(x_lo, x_hi)])


def riemann_sum_g(x_lo, x_hi, n):
    length = x_hi - x_lo
    segment_length = length / n
    return sum(g(x_lo + i * segment_length) * segment_length for i in range(n))


def riemann_sum(f, x_lo, x_hi, n):
    length = x_hi - x_lo
    segment_length = length / n
    return sum(f(x_lo + i * segment_length) * segment_length for i in range(n))


def almost_equals(a, b):
    return abs(a - b) < 0.0000001


def test_riemann_sum():
    test_riemann_sum_using_g()
    test_riemann_sum_using_square()
    test_riemann_sum_using_linear()


def test_riemann_sum_using_g():
    print("Tester riemann_sum med funksjonen g... ", end="")
    assert almost_equals(7.125, riemann_sum(g, 4, 6, 2))
    assert almost_equals(6.71875, riemann_sum(g, 4, 6, 4))
    assert almost_equals(6.3348335, riemann_sum(g, 4, 6, 1000))

    assert almost_equals(23.75, riemann_sum(g, 1, 5, 4))
    assert almost_equals(22.4375, riemann_sum(g, 1, 5, 8))
    assert almost_equals(21.166676666, riemann_sum(g, 1, 5, 1_000_000))
    print("OK")


def test_riemann_sum_using_square():
    def square(x):
        return x**2

    ## Arealet under grafen square(x) = x**2 mellom 1 og 3
    ## Eksakt svar  er 8 + 2/3, altså 8.66666666....
    ## Merk at vi kommer gradvis nærmere eksakt svar ved å øke n
    print("Tester riemann_sum med funksjonen square... ", end="")
    assert almost_equals(5.0, riemann_sum(square, 1, 3, 2))
    assert almost_equals(7.88, riemann_sum(square, 1, 3, 10))
    assert almost_equals(8.5868, riemann_sum(square, 1, 3, 100))
    print("OK")


def test_riemann_sum_using_linear():
    def linear(x):
        return x

    ## Arealet under grafen for funksjonen f(x) = x mellom 2 og 4
    ## Eksakt svar er 6.
    ## Merk at vi kommer gradvis nærmere riktig svar ved å øke n
    print("Tester riemann_sum med funksjonen linear... ", end="")
    assert almost_equals(5.0, riemann_sum(linear, 2, 4, 2))
    assert almost_equals(5.5, riemann_sum(linear, 2, 4, 4))
    assert almost_equals(5.998046875, riemann_sum(linear, 2, 4, 1024))
    print("OK")


test_riemann_sum_using_linear()
test_riemann_sum_using_square()
test_riemann_sum_using_g()
