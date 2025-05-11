class Vehicle:
    def start(self):
        print("Vehicle start")


    def call_engine(self):
        print("Vehicle call engine")
        self.__engine()

    # private method
    def __engine(self):
        print("Vehicle engine")


class Car(Vehicle):

    def start(self):
        print("Car start")

    def color(self):
        print("Car color")

x1 = Car()
x1.start()
x1.call_engine()
x1.color()