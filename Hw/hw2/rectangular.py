import turtle
class Rectangular:
    def __init__(self):
        self.length = int(input('length:'))
        self.width = int(input('width:'))
    @property
    def calc_perimeter(self):
        return (self.length * 2) + (self.width * 2)
    @property
    def calc_area(self):
        return self.length * self.width
    @property
    def show(self):
        return (f'width = {self.width} \nlength = {self.length} \nperimeter = {self.calc_perimeter} \narea = {self.calc_area}')

#for example and test attribute
a = Rectangular()
print(a.show)

