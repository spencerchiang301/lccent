class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = None
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or age > 100:
            raise ValueError("age must be between 0 and 100")
        else:
            self._age = age

user1 = Person("John", 18)
print(user1.age)
user1.age = 101