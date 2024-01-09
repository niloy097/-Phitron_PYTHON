from abc import ABC, abstractclassmethod

class Polygon(ABC):
    @abstractclassmethod
    def noofSides(self):
        pass

class Triangle(Polygon):
    def noofSides(self):
        print("I have 3 sides")
    
class Pentagon(Polygon):
    def noofSides(self):
        print("I have 5 sides")
        

tri = Triangle()
pen = Pentagon()

tri.noofSides()
pen.noofSides()