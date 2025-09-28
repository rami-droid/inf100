
def get_endpoints(i, n, x_lo, x_hi):
    "x lo and x hi are floats"

    length = x_hi - x_lo
    segment_length = length / n
    start = x_lo + i * segment_length
    end = start + segment_length

    return (start, end)


def almost_equals(a, b):
    return abs(a - b) < 0.000000001

def test_get_endpoints():
    print('Testing get_endpoints... ', end='')
    start, end = get_endpoints(1, 4, 50.0, 150.0)
    assert almost_equals(75, start)
    assert almost_equals(100, end)

    start, end = get_endpoints(3, 4, 50.0, 150.0)
    assert almost_equals(125, start)
    assert almost_equals(150, end)

    start, end = get_endpoints(0, 3, -30, 60)
    assert almost_equals(-30, start)
    assert almost_equals(0, end)
    print('OK')


def main():
    x_lo = float(input('x_lo = \n'))
    x_hi = float(input('x_hi = \n'))
    n = int(input('n = \n'))

    for i in range(n):
        print(f'{str(get_endpoints(i, n, x_lo, x_hi)).strip('()').replace(",", "")}')

if __name__ == '__main__':
    main()