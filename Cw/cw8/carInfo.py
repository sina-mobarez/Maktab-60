class CarInfo:
    def __init__(self, brand, year, model):
        self.brand = brand
        self.model = model
        self.year = year

    def get_car_detail(self):
        return f'Brand: {self.brand} >> Model: {self.model} >> Year: {self.year}'

    def get_car_brand(self):
        return f'Brand : {self.brand}'

    def get_car_model(self):
        return f' Model : {self.model}'
