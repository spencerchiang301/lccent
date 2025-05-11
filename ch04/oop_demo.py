class Vehicle:
    def __init__(self):
        pass

    def start(self):
        print('Start - Vehicle')

class Car(Vehicle):
    def __init__(self):
        pass

    def start(self):
        print('Start - Car')
        self.stop()

    def stop(self):
        print('Stop - Car')

class Trunk(Vehicle):
    def start(self):
        super().start()
        print('Start - Trunk')

class Motor(Car):
    def start(self):
        super().start()
        print('Start - Motor')

# car = Car()
# car.start()

# trunk = Trunk()
# trunk.start()
#
motor = Motor()
motor.start()

