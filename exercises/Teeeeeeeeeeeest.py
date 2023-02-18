class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):

        longname = f"{self.make} {self.model} {self.year}"
        return longname.title()

    def read_odometer(self):
        print("The car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot return back the odometer, you prick !!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_life = 40

    def describe_battery(self):
        return self.battery_life

my_el_car = ElectricCar("Tesla", "M", "2018")
print(my_el_car.get_descriptive_name())











