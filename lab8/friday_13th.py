from datetime import datetime
from datetime import timedelta 

def first_friday_13th_after(date):
    start = datetime.date(date)
    days_ahead = 1

    while True:
        next_date = start + timedelta(days=days_ahead)
        if next_date.day == 13 and next_date.weekday() == 4:
            return next_date
        days_ahead += 1


def test_first_friday_13th_after():
    print('Tester first_friday_13th_after... ', end='')
    # Test 1
    result = first_friday_13th_after(datetime(2022, 10, 24))
    assert (2023, 1, 13) == (result.year, result.month, result.day)
    # Test 2
    result = first_friday_13th_after(datetime(2023, 1, 13))
    assert (2023, 10, 13) == (result.year, result.month, result.day)
    # Test 3
    result = first_friday_13th_after(datetime(1950, 1, 1))
    assert (1950, 1, 13) == (result.year, result.month, result.day)
    print('OK')
