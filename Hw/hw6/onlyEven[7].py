# raise exception for odd numbers
def check_even(n):
    if (n % 2) != 0:
        raise TypeError(f'your number is odd')


# define a decorator to check enter just even numbers
# use *args for use decorator anywhere
def only_even(func):
    def wrapper(*args, **kwargs):
        try:
            check_even(args[0])
            check_even(args[1])
            x = func(args[0], args[1])
            return x
        except TypeError:
            return f"Please add even numbers "

    return wrapper


# define a function that plus 2 numbers
@only_even
def plus(a, b):
    return a + b


print(plus(3, 4))
print(plus(2, 6))
