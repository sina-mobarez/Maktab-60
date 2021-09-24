import math


def check(r):
    if r <= 0:
        raise TypeError(f'the input must be bigger than zero and {r} is not')
    else:
        return r


class Sphere:
    def __init__(self, r):
        self.r = r

    @property
    def calc_area(self):
        a = check(self.r)
        return f' area of sphere is : {(4 * math.pi * (a ** 2))}'

    @property
    def calc_volume(self):
        v = check(self.r)
        return f' volume of sphere is : {(4 / 3) * math.pi * (v ** 3)}'


b = Sphere(4)
c = b.calc_volume
print(c)
x = Sphere(0)
x.calc_area
