class Vehicle:
   def start(self):
       print("Vehicle Start")

   def speed(self):
       print("Vehicle speed")

   def forward(self):
       print("Vehicle forward")

class Car(Vehicle):
    def start(self):
        print("Car start")

    def stop(self):
        print("Car stop")


x1 = Car()
x1.start()
x1.forward()
x1.stop()


