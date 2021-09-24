import random


class Shooter:
    sybl_distance = 500
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.differ = (self.height - self.weight) * (0.5 + (random.random() * (2 - 0.5)))
        self.differ = Shooter.sybl_distance - self.differ

class Database:
    def __init__(self):
        self.result = {}
    def add_shooter(self, shooter):
        shoot = {
            'differ': shooter.differ,
            'height': shooter.height,
            'weight': shooter.weight
        }
        self.result.update({shooter.name: shoot})
    @property
    def get_average(self):
        differ_list = []
        for key, value in self.result.items():
            differ_list.append(value['differ'])
        return round(sum(differ_list) / len(differ_list), 2)
    @property
    def sort_by_differ(self):
        differ_list = []
        for key, value in self.result.items():
            differ_list.append(value['differ'])
        differ_list = sorted(differ_list)
        differ_list = reversed(differ_list)
        sort_result = []
        for i in differ_list:
            for key, value in self.result.items():
                if value['differ'] == i:
                    dic = {
                        key: value
                    }
                    sort_result.append(dic)
                    continue
        return sort_result


a = Shooter('ali', 170, 56)
a2 = Shooter('sina', 190, 78)
a3 = Shooter('saeed', 187, 62)
a4 = Shooter('hosein', 172, 67)
a5 = Shooter('hasan', 165, 60)
db = Database()
db.add_shooter(a)
db.add_shooter(a2)
db.add_shooter(a3)
db.add_shooter(a4)
db.add_shooter(a5)
print(db.result)
print(db.get_average)
print(db.sort_by_differ)
