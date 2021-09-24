# define a decorator for double result of a function
# use *args for use decorator anywhere
def double(func):
    def wrapper(*args, **kwargs):
        x = func(args[0], args[1])
        return 2 * x

    return wrapper


# define a function to plus numbers
@double
def plus(a, b):
    return a + b


print(plus(5, 5))
