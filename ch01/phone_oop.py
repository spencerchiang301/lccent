class Phone:
    def __init__(self, brand):
        self.brand = brand

    def call(self):
        print(f"{self.brand}: Calling function")

    def camera(self):
        print(f"{self.brand}: Camera function")

    def message(self):
        print(f"{self.brand}: Message function")

    def calculate(self):
        print(f"{self.brand}: Calculate function")

    def calendar(self):
        print(f"{self.brand}: Calendar function")

    def navigate(self):
        print(f"{self.brand}: Navigate")

    def note(self):
        print(f"{self.brand}: Note function")

    def basic(self):
        self.call()
        self.camera()
        self.message()
        self.calculate()
        self.calendar()
        self.navigate()
        self.note()
        print("================================")

    def low_level(self):
        self.call()
        self.camera()
        print("================================")


iphone_6 = Phone("Iphone_6")
iphone_6.basic()

iphone_6_low_level = Phone("Iphone_6_low_level")
iphone_6_low_level.low_level()

iphone_7 = Phone("Iphone_7")
iphone_7.basic()