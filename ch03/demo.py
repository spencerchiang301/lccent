# parent
class Car:
    def __init__(self, car_type, car_size):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def forward(self):
        pass

    def backward(self):
        pass

    def speed(self):
        pass

    def navigate(self):
        pass

class X1Car(Car):
    def __init__(self, car_type, car_size):
        super().__init__(car_type, car_size)

    def color(self):
        pass


x1 = X1Car('X1', 's')
x1.speed()
x1.forward()
x1.color()
