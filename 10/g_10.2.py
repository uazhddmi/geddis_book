class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def break_(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

car = Car(1983, 'Japan')

for i in range(5):
    car.accelerate()
    print(f"Car's actual speed is {car.get_speed()}")

for i in range(5):
    car.break_()
    print(f"Car's actual speed is {car.get_speed()}")

