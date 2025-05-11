from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def drive(self):
        pass

    def stop(self):
        pass


c1 = Car()
c1.start()
