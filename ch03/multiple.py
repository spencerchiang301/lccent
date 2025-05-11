class Gps:
    def navigate(self):
        print('Nagivate - GPS')

    def start(self):
        print('Start - GPS')


class MusicPlayer:
    def play_music(self):
        print('Play Music')

    def navigate(self):
        print('Navigate - Music')

class Car1():
    pass

class Car2(MusicPlayer, Gps):
    pass

car1 = Car1()
car1.start()
car1.navigate()
print("===================================")
car2 = Car2()
car2.start()
car2.navigate()




