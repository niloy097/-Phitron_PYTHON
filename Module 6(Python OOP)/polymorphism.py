class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def makes_sound(self):
        print("Making Sound")


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print("Meaooooow")


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def makes_sound(self):
        print("Gheow, Gheow")

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def makes_sound(self):
        print("Behhh beeh beeh")
        
don = Cat("Real Don")
don.makes_sound()

shepard = Dog("Local Shepard")
shepard.makes_sound()

mess = Goat("L M")
mess.makes_sound()

less = Goat("gora gori khay")

animals = [don, shepard, mess, less]

for animal in animals:
    animal.makes_sound()