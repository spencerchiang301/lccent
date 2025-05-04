class Person:
    count = 0
    def __init__(self, name, age=20):
        self.name = name
        self.age = age

    def change_gender(self, gender):
        self.__gender = gender

    def say_hello(self):
        print("Hello " + self.name)

    def show_info(self):
        print(self.name)
        print(self.age)


user1 = Person("John", 25)
user1.show_info()



