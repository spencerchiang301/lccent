class CreaitCard:
    def __init__(self, card_number):
        self.__card_number = card_number

    def get_card_number(self):
        return "****-****-****-" + self.__card_number[-4:]


a = CreaitCard("123424324231423")
print(a.get_card_number())
print(CreaitCard.__card_number)