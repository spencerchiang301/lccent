class Vehicle:
    # constructor
    def __init__(self, car_name, car_type='Toyota'):
        self.car_name = car_name
        self.car_type = car_type

    def start(self):
        print("Vehicle start")

    def stop(self):
        print("Vehicle stop")

    def color(self):
        print("Vehicle color")

    def show_info(self):
        print(f"{self.car_name}/{self.car_type} ")


class Car1(Vehicle):
    def __init__(self):
        super().__init__('Car1')

    def start(self):
        super().start()
        print("Car1 start")


x1 = Car1()
x1.start()
x1.show_info()