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
