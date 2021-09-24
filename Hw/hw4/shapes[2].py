import math


class Shape:
    def __init__(self, width):
        self.width = width


class Square(Shape):
    pass

    @property
    def calc_area(self):
        print(self.width * self.width)

    @property
    def calc_perimeter(self):
        print(self.width * 4)

    @property
    def draw(self):
        for i in range(self.width):
            print('*  ' * self.width)


class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__(width)
        self.length = length

    @property
    def calc_area(self):
        print(self.width * self.length)

    @property
    def calc_perimeter(self):
        print((self.width * 2) + (self.length * 2))

    @property
    def draw(self):
        for i in range(self.length):
            print('  *' * self.width)


class Parallelogram(Shape):
    def __init__(self, width, height, length_for_calc_p):
        super().__init__(width)
        self.height = height
        self.length = length_for_calc_p

    @property
    def calc_area(self):
        print(self.width * self.height)

    @property
    def calc_perimeter(self):
        print(2 * (self.width + self.length))

    # for drawing Parallelogram you must give 3 arg to program and always length > height if not the shape couldn't be
    # Parallelogram
    @property
    def draw(self):
        for i in range(self.height):
            print(' ' * ((self.width - 1) - i) + '  *' * ((self.width - 1) + 1))


class Rhombus(Shape):
    def __init__(self, width):
        super().__init__(width)
        self.height = self.width / math.sqrt(2)

    @property
    def calc_area(self):
        print(self.width * self.height)

    @property
    def calc_perimeter(self):
        print(self.width * 4)

    @property
    def draw(self):
        height = round(self.height)
        for i in range(height):
            print(' ' * ((self.width - 1) - i) + '  *' * ((self.width - 1) + 1))


class Diamond(Shape):
    pass

    @property
    def calc_area(self):
        print(self.width * self.width)

    @property
    def calc_perimeter(self):
        print(self.width * 4)

    @property
    def draw(self):
        for i in range(1, self.width+1):
            print(' ' * (self.width-i) + '* ' * i)
        for i in range(self.width-1, 0, -1):
            print(' ' * (self.width-i) + '* ' * i)


a = Parallelogram(6, 4, 5)
a.draw
