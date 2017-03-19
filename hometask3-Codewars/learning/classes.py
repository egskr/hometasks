class Car(object):
    created_cars_count = 0
    def __init__(self, velocity, model, color):
        print(self)
        print("__init__ called")
        self.velocity = velocity
        self.model = model

        self.color = color

        Car.created_cars_count += 1

    def move(self):
        print(self.velocity)
    def display_info(self):  #self - eto ekzemplyar klassa, naprimer car1  Car.display_info(car1)
        print(self.model)    # mozhno vmesto self ispolz lyuboe "aeafae" - tozhe ok
        print(self.color)
        print("Car number: {}".format(Car.created_cars_count))
    def get_motor_type(self):
        return "BLA"

car1 = Car(100, "bmw", "white")
car2 = Car(90, "ford", "green")

car1.display_info()
print(car2.get_motor_type())



######INHERITANCE
class SportCar(Car):  # nasleduem car
    def __init__(self, sport):
        self.sport = sport
        super()
    def display_sport(self):
        pass

sport1 = SportCar()

#Car.display_info(car1) ====== car1 = Car(100, "bmw", "white"); car1.display_info()
#v skobki podstavitsya car1