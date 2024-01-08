from abc import ABC, abstractclassmethod
#abstract base class
class Animal:
    @abstractclassmethod #enforce all derived class to have a eat method
    def eat(self):
        print("Hey nana! eating banana") 
    
    @abstractclassmethod
    def move(self):
        pass
    
class Monkey(Animal):
    def __init__(self, name) -> None:
        self.catagory = "Monkey"
        self.name = name
        super().__init__()
    def eat(self):
        print("Hey na na na, I am eating Banana")
        
    def move(self):
        print("Hanging on the tree")
        
layka = Monkey("Lucky")
layka.eat()
layka.move()