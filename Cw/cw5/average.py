import random


class Student:
    max_average = 20
    def __init__(self):
        self.name = input('name :')
        self.family = input('family :')
        self.average = random.randint(1, 21)
        self.differ = Student.max_average - self.average
name = []
differ = []
for i in range(5):
    a = Student()
    name.append(a.name)
    differ.append(a.differ)
for i in range(5):
    print(f'{name[i]} , {differ[i]}')



