# define a generator that make a divisibility next number
# range 100000 for taking easy to hardware
def get_next_multiple(n):
    i = 0
    while True:
        i += 1
        if (i % n) == 0:
            yield i

g = get_next_multiple(2)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
b = get_next_multiple(13)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))