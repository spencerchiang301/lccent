class Car:
    def drive(self, speed):
        print(f'Car at {speed}')


class Trunk:
    def drive(self, speed):
        print(f'Trunk at {speed}')

class Trunk2:
    def drive(self, speed):
        print(f'Trunk2 at ', speed * 2)

class Trunk3:
    def drive(self, speed):
        print(f'Trunk3 at ', speed * 3 + 20)

class Trunk4:
    def drive(self, speed):
        print(f'Trunk4 at ', speed * 4 + 20)

class Trunk5:
    def drive(self, speed):
        print(f'Trunk5 at ', speed * 5 + 20 / 4)

c3 = Trunk3()
c3.drive(100)

c4 = Trunk4()
c4.drive(100)

