class Machine():
    def power_on(self):
        print('Power on - Vehicle1')

class Vehicle(Machine):
    def move(self):
        print('Move - Vehicle')

    def power_off(self):
        print('Power off - Vehicle1')

class Car(Vehicle):
    def start(self):
        print('Start - Car')

class Car2(Vehicle):
    def start(self):
        print('Start - Car')

ford = Car()
ford.start()
ford.move()
ford.power_on()
ford.power_off()

toyota = Car()
toyota.start()
toyota.power_off()