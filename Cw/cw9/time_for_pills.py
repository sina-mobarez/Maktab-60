import datetime


def pills_time():
    time_now = datetime.time(14, 00, 00)
    date_now = datetime.date(2018, 2, 19)
    date_time = datetime.datetime.combine(date_now, time_now)
    i = 0
    while True:
        if i < 9:
            add_hours = datetime.timedelta(hours=8)
            future_date = date_time + add_hours
            yield (f'its time for eat yours pills {date_time} and your next time for pills {future_date} >>> {9 - i} pills has remind')
            date_time = future_date
            i += 1
        else:
            print("your pills its over")
            break

x = pills_time()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
