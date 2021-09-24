class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    pass

    def capaciti(self):
        return print(f'the seating capacity of a {self.name} is {self.capacity} passengers')

    def fare(self):
        return super().fare() + self.capacity * 10


bus1 = Bus('volvo', 120, 24, 50)
print(bus1.fare())
