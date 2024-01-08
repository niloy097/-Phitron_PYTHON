class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def __repr__(self) -> str:
        return f"{self.name} {self.price}"
        
    def move(self):
        pass
    
class Buss(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACBus(Buss):
    def __init__(self, name, price, seat, tempera) -> None:
        self.tempera = tempera
        super().__init__(name, price, seat)
    
    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()
    
gree_line = ACBus("Green", 50000000, 40, 16)
print(gree_line)