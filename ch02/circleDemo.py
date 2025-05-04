import math


class CircleDemo:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return self.__radius * self.__radius * math.pi

    def change_radius(self, new_radius):
        self.__radius = new_radius

a = CircleDemo(2)
print(a.area())

a.change_radius(10)
print(a.area())
print(a.__dict__)

a.__radius = 100
print(a.area())
print(a.__dict__)