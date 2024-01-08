from math import pi
class Shape:
    def __init__(self, name) -> None:
        self.name = name
        
class Rectangel(Shape):
    def __init__(self, name, length, widht) -> None:
        self.length = length
        self.width = widht
        super().__init__(name)
        
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)
        
    def area(self):
        return pi * self.radius * self.radius

rec = Rectangel("Rectangle", 10, 10)
print(rec.area()) 

cir = Circle("Circle", 5)
print(cir.area())