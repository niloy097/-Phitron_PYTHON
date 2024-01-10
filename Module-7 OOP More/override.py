class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def eat(self):
        print("Vat Mangsho Polaw")

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    def eat(self):
        print("Vegetables")
        
    
    def exercise(self):
        print("Gym")
    
    
    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self, other):
        return self.weight * other.weight
    
    def __len__(self):
        return self.height

    def __gt__(self, other):
        return self.age > other.age


Sakib = Cricketer("Sakib", 36, 150, 76, "BD")
mushi = Cricketer("Mushi", 23, 23, 45, "BD")
# Sakib.eat()
# Sakib.exercise()


#plus sign overloadding(dunder method)
print(4 + 5)
print("Sakib" + "Rakib")
print([12, 98] + [5, 6, 7, 1, 2])
print(Sakib + mushi)
print(Sakib * mushi)
print(len(Sakib))
print(Sakib > mushi)