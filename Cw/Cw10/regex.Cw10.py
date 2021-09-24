from datetime import timedelta
from datetime import datetime, date
import re
from time import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


def name(name):
    return re.search("^[A-Za-z][A-Za-z]+ [A-Za-z]+", name)


print(name("ali sadi"))


def cell(cell):
    return re.search("\A09\d{9}", cell)


@timer_func
def email(email):
    return re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)


email("aaagmail@g.com")


def password(password):
    password = input("Enter string to test: ")
    if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return True
    else:
        return False


@timer_func
def date_time(date_time):
    if re.search(r'\d{4}/\d{1,2}/\d{1,2}', date_time):
        return True
    else:
        return False


def age(*args):
    birth = date(*args)
    now_time = date.today()
    print(now_time.year-birth.year)

    a = birth.replace(year=now_time.year)
    if now_time > a:
        print(now_time-a)
    else:
        print(timedelta(days=365)+now_time-a)


age(2020, 9, 10)
