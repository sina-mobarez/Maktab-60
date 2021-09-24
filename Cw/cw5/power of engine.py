import random


class Engine:
    engine = 1000
    def __init__(self):
        self.speed = random.randint(1, 101)
        self.torque = Engine.engine / self.speed


list_speed = []
list_torque = []
for i in range(10):
    a = Engine()
    list_speed.append(a.speed)
    list_torque.append(a.torque)
ave_speed = sum(list_speed) / 10
ave_torque = sum(list_torque) / 10
print(ave_torque)
print(ave_speed)


