def logged(function):
    def wrapper(*args, **kwargs):
        print(f'you called {function.__name__}{args}')
        res = function(*args, **kwargs)
        print(f'it returned {res}')
        return res

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


func(4, 4, 4, )
