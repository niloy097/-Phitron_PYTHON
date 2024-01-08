#encapsulation --> hide details
#access modifer: public, protected, private

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name #public data
        self._brach = "banani 11" #a convention(protected data)
        self.__balance = initial_deposit #private data
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_Banlance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f"Fakira Taka Nai"
            
        
rafsun = Bank("Chootto Bro", 10000)

print(rafsun.holder_name)
rafsun.deposit(40000)
print(rafsun.get_Banlance())
print(rafsun._brach)

#Kahini kore private balance dekha jay-->
print(rafsun._Bank__balance)
