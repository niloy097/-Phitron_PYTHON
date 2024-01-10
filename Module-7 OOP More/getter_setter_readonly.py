#read only --> you cannot set the value, value cannot be changed
#getter --> get a value of a property through a method, Most of the time, you will get the value of a private property
#setter --> set a value of a property through a method, Most of the time, you will set the value of a private property
class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money
    
    @property #getter without any setter is readonly attribute
    def get_money(self):
        return self.__money
    @property #getter without any setter is readonly attribute
    def salary(self):
        return self.__money
    
    #setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return "Neg. sallary is not legal"
        self.__money += value

samsu = User("Kopa", 21, 10000)
# print(samsu.__money) 
print(samsu.get_money)
print(samsu.salary)
samsu.salary = 4500
print(samsu.salary)