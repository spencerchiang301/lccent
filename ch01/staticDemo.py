class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    #method
    def get_bmi(self):
        return Person.calc_bmi(self.weight, self.height)

    @staticmethod
    def calc_bmi(weight, height_cm):
        height = height_cm / 100
        return round(weight/ (height **2), 2)


    @classmethod
    def from_data(cls, data):
        return cls(data["name"], data["weight"], data["height"])


def bye():
    print("Bye")

# user1 = Person("John", 35, 160)
# print("BMi of user1: ", user1.get_bmi())

data = {"name":"Tom", "weight":44, "height":166}
user2 = Person.from_data(data)
print("BMi of user2: ", user2.get_bmi())
bye()


# print("BMI of user3: ", Person.calc_bmi(32, 175))
