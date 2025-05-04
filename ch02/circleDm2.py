import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):
        return self.__radius * self.__radius * math.pi

    def area2(self):
        return self.__radius * self.__radius * math.pi


    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value

    def set_radis(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value

c1 = Circle(2)
# not call c1.area()
print(c1.area)
print(c1.area2())
print(c1.area2)
#------------------------
# c1.__radius = 10
# print(c1.area)
# print(c1.__dict__)
#------------------------
c1.radius = 10  # call line 19
print(c1.radius)
print(c1.area)
#------------------------

c1.set_radis(100)
print(c1.radius)
print(c1.area)
