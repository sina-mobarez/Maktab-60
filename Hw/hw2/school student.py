class Student:
    def __init__(self):
        self.height, self.weight, self.age = list(map(int, input('height: , weight: , age: ').split()))
        self.lst = self.height, self.weight, self.age
class SchoolClass:
    def __init__(self):
        self.number = int(input('number of student:'))
        self.list_age = []
        self.list_height = []
        self.list_weight = []
        for i in range(self.number):
            x = Student().lst
            self.list_height.append(x[0])
            self.list_weight.append(x[1])
            self.list_age.append(x[2])
a = SchoolClass()
b = SchoolClass()
class ShowAverage:
    def __init__(self):
        n = a.number
        age = a.list_age
        age2 = b.list_age
        weight = a.list_weight
        weight2 = b.list_weight
        height = a.list_height
        height2 = b.list_height
        print(sum(age)/n)
        print(sum(height)/n)
        print(sum(weight)/n)
        print(sum(age2)/n)
        print(sum(height2)/n)
        print(sum(weight2)/2)
        if (sum(height) / n) > (sum(height2) / n):
            print('A')
        elif (sum(height) / n) < (sum(height2) / n):
            print('B')
        elif (sum(height) / n) == (sum(height2) / n):
            if (sum(weight) / n) > (sum(weight2) / n):
                print('B')
            elif (sum(weight) / n) < (sum(weight2) / n):
                print('A')
            else:
                print('Same')


c = ShowAverage()