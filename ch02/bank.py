class Bank:
    def __init__(self, money, name):
        self.__money = money
        self.name = name

    def money_out(self, n):
        self.__money -= n

    def money_in(self, n):
        if n < 0:
            print("Not allowed negative money")
        else:
            self.__money += n

    def total(self):
        return self.__money

    def show_info(self):
        return self.name


user1 = Bank(100, 'jack')
print(user1.total())
print(user1.show_info())

user1.__money=1000000
print(user1.total())
print(user1.show_info())