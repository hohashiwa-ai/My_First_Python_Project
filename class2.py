class Car:

    raise_amount = 1.08
    def __init__(self, brand , color, price):
        self.brand = brand
        self.color = color
        self.price = price
        self.email = brand + '.' + color + '@company.com'

    def apply_raise(self):
        self.price = int(self.price * self.raise_amount)


    def fullname(self):
        return f"{self.brand}\n {self.color}\n {self.price}\n {self.email}"

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls , car_str):
        brand, color, price = car_str.split('-')
        return cls(brand , color , price)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


car1 = Car("Ford","Black",20000)
car2 = Car("Honda","white",30000)


