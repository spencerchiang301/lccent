class Vehicle:
    def __init__(self, brand, base_rate):
        self.brand = brand
        self.base_rate = base_rate

    def rental_price(self, days):
        return self.base_rate * days

    def description(self):
        return f'{self.brand} Vehicle'

    def info(self):
        print(self.description())
        print(f"Base rate: ${self.base_rate}/day")


class Car(Vehicle):
    def __init__(self, brand, base_rate, model, seats):
        super().__init__(brand, base_rate)
        self.model = model
        self.seats = seats

    def rental_price(self, days):
        return super().rental_price(days) + 50

    def description(self):
        return f'{self.brand} {self.model} (Car with {self.seats} seats)'

def print_rental_summary(vehicle: Vehicle, days: int):
    vehicle.info()
    print(f"Total rental for {days} days: ${vehicle.rental_price(days)}")
    print("-" * 40)

v1 = Car('Toyota', 100, 'Camry', 5)
print_rental_summary(v1, 3)