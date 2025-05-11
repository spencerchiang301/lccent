from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        self.authenticate()
        self.pay()
        self.send_receipt()

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self):
        pass

    def send_receipt(self):
        print(f"bank: Paid$ {self.amount}")

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def authenticate(self):
        print(f"Authenticated card number: {self.card_number[-4:]}...")

    def pay(self):
        print(f"Payment amount : {self.amount}...")


class LinePayProcessor(PaymentProcessor):
    def __init__(self, amount, line_id):
        super().__init__(amount)
        self.line_id = line_id

    def authenticate(self):
        print(f"Authenticated line id: {self.line_id}...")

    def pay(self):
        print(f"Payment amount : {self.amount}...")


card1 = CreditCardProcessor(20000, "1234567890")
card1.process()
print("================================================================")

line = LinePayProcessor(100, "jack wang")
line.process()