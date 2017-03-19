#!/usr/bin/python

class Car():
    car_quantity = 0
    def __init__(self, color, power, year):
        self.color = color
        self.power = power
        self.year = year

        Car.car_quantity += 1

    def display_param(self):
        pass
        print("Color: {}".format(self.color))
        print("Power: {}".format(self.power))
        print("Year: {}".format(self.year))

    def show_quantity():
        print(Car.car_quantity)


car1 = Car("green", "200kw", "2014")
car2 = Car("red", "150kw", "1999")

carlist = [car1, car2]

for i in carlist:
    print("Car :")

    i.display_param()


class SportCars(Car):
    def __init__(self, color, power, year):
        self.color = color
        self.power = power
        self.year = year

    def show_carinfo(self):
        print(self.year)

scar1 = SportCars("black", "860kw", "2000")
scar1.display_param()






