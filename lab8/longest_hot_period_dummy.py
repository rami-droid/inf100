def longest_hot_period(temperatures, threshold):
    longest_start = longest_end = -1
    current_start = None
    longest_length = 0

    for i, temp in enumerate(temperatures):
        if temp >= threshold:
            if current_start is None:
                current_start = i
        else:
            if current_start is not None:
                length = i - current_start
                if length > longest_length:
                    longest_length = length
                    longest_start = current_start
                    longest_end = i
                current_start = None

    # Handle case where period extends to end of list
    if current_start is not None:
        length = len(temperatures) - current_start
        if length > longest_length:
            longest_start = current_start
            longest_end = len(temperatures)

    return (longest_start, longest_end)

def test_longest_hot_period():
    print('Testing longest_hot_period... ', end='')
    temps = [25, 23, 19, 22, 24, 25, 21, 25, 26]

    threshold = 22
    expected_start, expected_end = 3, 6
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 23
    expected_start, expected_end = 0, 2
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 15
    expected_start, expected_end = 0, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 21
    expected_start, expected_end = 3, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 25
    expected_start, expected_end = 7, 9
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    threshold = 30
    expected_start, expected_end = -1, -1
    actual_start, actual_end = longest_hot_period(temps, threshold)
    assert (expected_start, expected_end) == (actual_start, actual_end)

    print('OK')

if __name__ == '__main__':
    test_longest_hot_period()
