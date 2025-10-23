def total_income(path):
    with open(path, 'r') as f:
        sum = 0
        content = f.read().splitlines()
        table = [row.split(',') for row in content]
        for items in table[1:]:
            sum += (int(items[2]) - int(items[1])) * int(items[3])
    return sum


def test_total_income():
    print('Tester total_income... ', end='')
    expected = (
        (50 - 10) * 100
        + (100 - 20) * 50
        + (500 - 50) * 10
        + (1000 - 100) * 5
        + (10000 - 500) * 2
    )
    actual = total_income('sales.csv')
    assert expected == actual, f'{expected=}, {actual=}'
    print('OK')

test_total_income()
