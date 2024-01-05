class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
    
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount
    
    def withdraw(self, am):
        if am < self.min_withdraw:
            return f"Fokira, you can't withdraw below {self.min_withdraw}"
        elif am > self.max_withdraw:
            return f"Bank Fakir hoye jabe, You can't with draw more than {self.max_withdraw}"
        else:
            self.balance -= am
            print(f"Your balanace after withdraw {self.get_balance()}")
            print(f"Here is your money {am}")
        
brac = Bank(15000)
print(brac.withdraw(25))
print(brac.withdraw(23434234234))
brac.withdraw(1000)

dbbl = Bank(5000)
dbbl.deposit(2000)
dbbl.deposit(2000)
print(dbbl.get_balance())