# #Protected class--> accessible in parent and child class only
# class Base:
#     def __init__(self):
#         self._a = 2
    
# class Derived(Base):
#     def __init__(self):
        
#         Base.__init__(self)
#         print("Calling the protected member of base class: ", self._a)
        
        
#         self._a = 3
#         print("Calling modified member outside class: ", self._a)

# obj1 = Derived()
# obj2 = Base()

# print("Accessing protected member of obj1: ", obj1._a)
# print("Accessing protected member of obj2: ", obj2._a)


#Private Data:-->
class Base:
    def __init__(self, name):
        self.__name = name
    def showName(self):
        return f"My name is: {self.__name}"
niloy = Base("Niloy")
print(niloy.showName())