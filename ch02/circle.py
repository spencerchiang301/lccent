import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return self.__radius * self.__radius * math.pi

c1 = Circle(10)
print(c1.area)

c1.__area = 30
print(c1.area)
