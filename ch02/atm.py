class ATM:
    def __init__(self, pin, balance):
        self.__pin_code = pin
        self.__balance = balance

    def withdraw(self, pin, amount):
        if not self.__verfiy_pin(pin):
            print("PIN not verified")
        else:
            if amount > self.__balance:
                print("Not enough money")
            else:
                self.__balance -= amount
                print("after withdraw, total balance is:", self.__balance)

    def __verfiy_pin(self, input_pin):
        return input_pin == self.__pin_code


atm = ATM("1234", 5000)
# 第一次輸錯密碼, 不允許提款
atm.withdraw("9999", 1000)

# 第二次密碼對了, 就允許提款
atm.withdraw("1234", 1000)

# 不允許公開存取
#atm.__verify_pin("1234")


