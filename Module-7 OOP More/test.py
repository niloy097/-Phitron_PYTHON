#compositon--> choto bhai of inheritance
#inheritance is a IS-a relationship where composition is a Has-a Relationship

class CPU:
    def __init__(self, type) -> None:
        self.type = type
    
    def show_Deatils(self):
        print("This a set of computers part")

class RAM:
    def __init__(self, size) -> None:
        self.size = size
    
    def show_Detals(self):
        print(f"Ths size of this ram is: {self.size}")

class SSD:
    def __init__(self, storage):
        self.storage = storage
    def show_Details(self):
        print(f"The Storage is: {self.storage}")
        

class Computer:
    def __init__(self, type, ram_size, storage):
        self.type = CPU(type)
        self.ram = RAM(ram_size)
        self.stor = SSD(storage)

my_pc = Computer("PC", 32, 120)
my_pc.type.show_Deatils()
my_pc.ram.show_Detals()
my_pc.stor.show_Details()