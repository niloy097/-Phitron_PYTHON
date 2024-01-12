#Inheritance vs Composition

class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores


class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity

#Computer has a CPU
#Computer has a RAM
#Computer has a HD
class Computer:
    def __init__(self, cores, ram_size, hd_cap) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hd = HardDrive(hd_cap)
        
        
my_mac = Computer(8, 16, 512)
