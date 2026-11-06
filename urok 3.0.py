class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"No passengers in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")
car2 = Auto("BMW")

car.add_passenger(nick, kate)
car.print_passengers_names()
# a = 1; b = "string"; list = [1,"string"]