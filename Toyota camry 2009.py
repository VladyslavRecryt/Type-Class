class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2009)
    print(car.get_info())