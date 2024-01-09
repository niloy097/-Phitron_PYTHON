class Vehicle:
    def __init__(self, name) -> None:
        self.name = name
    
    def start(self):
        print("Starting")
        
class Bike(Vehicle):
    def __init__(self, name, model, cls) -> None:
        self.mode = model
        self.cls = cls
        super().__init__(name)
    
    def __repr__(self) -> str:
        return f"{self.name} {self.mode} {self.cls}"


bk = Bike("Pulser", 4323, "D")
print(bk)
