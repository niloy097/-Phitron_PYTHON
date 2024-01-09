class Bike:
    def __init__(self, name = "", gear = 0) -> None:
        self.name = name
        self.gear = gear
    def __repr__(self) -> str:
        return f"Name: {self.name}, Gear: {self.gear}"

honda = Bike("Honda", 5)
print(honda)
    