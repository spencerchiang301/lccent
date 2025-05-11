class Car:
    def start(self):
        print('Start - Car')

class Motor:
    def start(self):
        print('Start - Motor')

class Bicycle:
    def start(self):
        print('Start - Bicycle')


def run(vehicle):
    vehicle.start()


run(Bicycle())
run(Car())
run(Motor())