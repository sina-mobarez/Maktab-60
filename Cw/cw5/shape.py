class Shape:
    def __init__(self):
        self.length = int(input('enter length :'))
        self.width = int(input('enter width :'))
        self.tangle = int(input('enter tangle :'))
    @property
    def shape_of_(self):
        if self.width == self.length and self.tangle == 90:
            self.shape = 'square'
            print('square')
        elif self.width != self.length and self.tangle == 90:
            self.shape = 'rectangle'
            print('rectangle')
        elif self.width == self.length and self.tangle != 90:
            self.shape = 'rhombus'
            print('rhombus')
        elif self.width != self.length and self.tangle != 90:
            self.shape = 'parallelogram'
            print('parallelogram')
    @property
    def area(self):
        print(self.length * self.width)

a = Shape()
a.shape_of_
a.area