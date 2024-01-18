import random
import calendar, time
from bank import Bank
class Person:
    def __init__(self, str_name, str_email, str_address) -> None:
        self.name = str_name
        self.email = str_email
        self.address = str_address

class User(Person):
    max_loan_limit = 2
    my_balance = 0.0
    my_transaction_history = []
    def __init__(self, obj_bank, str_name, str_email, str_address) -> None:
        self.bank = obj_bank
        super().__init__(str_name, str_email, str_address)
    
    def create_an_account(self, int_password, str_account_type):
        self.password = int_password
        self.account_type = str_account_type
        self.account_number = random.randint(0, 1000)
        self.user_info = {
            
            'name' : self.name, 
            'email' : self.email,
            'address' : self.address,
            'password' : self.password,
            'account_type' : self.account_type,
            'account_number' : self.account_number,
            'balance' : self.my_balance
        }
        self.bank.user_list.append(self.user_info)
        
    def deposit_money(self, double_amount):
        flag = False
        for dictionary in self.bank.user_list:
            if self.name in dictionary['name']:
                flag = True
                dictionary['balance'] += double_amount
                self.bank.total_balance += double_amount
                tran_history = f"Successfully to deposite money to {self.name}'s account with amount {double_amount} tk"
                self.my_transaction_history.append(tran_history)
                self.bank.transaction_history.append(tran_history)
                break
        if flag is False:
           print("Account not found!!!!")
    
    def withdraw_amount(self, double_amount):
        flag = False
        for dictionary in self.bank.user_list:
            if self.name in dictionary['name']:
                flag = True
                if dictionary['balance'] >= double_amount:
                    if self.bank.total_balance < double_amount:
                        print("The Bank is Bankcrupt")
                        break
                    else:
                        print("Withdraw Money Successfully")
                        dictionary['balance'] -= double_amount
                        self.bank.total_balance -= double_amount
                        tran_history = f"Successfully to withdraw money from {self.name}'s account with amount {double_amount} tk"
                        self.my_transaction_history.append(tran_history)
                        self.bank.transaction_history.append(tran_history)
                        break
                else:
                    print("You don't have enough money for withdraw")
                    break
        if flag is False:
            print("Account not found!!")
                        
    
    def check_current_balance(self):
        flag = False
        for dictionary in self.bank.user_list:
            if self.name in dictionary['name']:
                flag = True
                return dictionary['balance']
        if flag is False:
            return f"Account not opened"
    
    def check_transaction_history(self):
        for history in self.my_transaction_history:
            print(history)
    
    def take_loan(self, double_amount, is_open):
        if(self.max_loan_limit > 0):
            if is_open == True:
                self.max_loan_limit -= 1
                flag = False
                for dictionary in self.bank.user_list:
                    if self.name in dictionary['name']:
                        flag = True
                        dictionary['balance'] += double_amount
                        self.bank.total_balance -= double_amount
                        self.bank.total_loan_balance += double_amount
                        print("Loan was given Successfully")
                        break
                if flag is False:
                    print("Account not found")
            else:
                print("Loan giving is closed")
        else:
            print("Loan limit exceeded")
    
    def transfer_amount(self, name, int_amount):
        flag = False
        for dictionary in self.bank.user_list:
            if name in dictionary['name']:
                flag = True
                dictionary['balance'] += int_amount
                break
        if flag is False:
            print("Account not found")
                
        for dictionary in self.bank.user_list:
            flag = False
            if self.name in dictionary['name']:
                flag = True
                dictionary['balance'] -= int_amount
                break

                 
        
        
class Admin(Person):
    # print("Admin")
    def __init__(self, obj_bank, str_name, str_email, str_address) -> None:
        self.bank = obj_bank
        super().__init__(str_name, str_email, str_address)
    
    def create_an_account(self, int_password):
        self.password = int_password
        user_info = {
            
            'name' : self.name, 
            'email' : self.email,
            'address' : self.address,
            'password' : self.password,
        }
        self.bank.admins.append(user_info)
            
    def delete_user_accout(self, str_user_name):
        flag = False
        for dictionary in self.bank.user_list:
            if str_user_name in dictionary['name']:
                flag = True
                self.bank.user_list.remove(dictionary)
                break
        if flag is False:
            print("User dosen't exists")
    
    def view_all_user_list(self):
        for dictionary in self.bank.user_list:
            print(f"Name: {dictionary['name']}, Email: {dictionary['email']}, Balance: {dictionary['balance']}")
    
    def view_all_admin_list(self):
        for dictionary in self.bank.admins:
            print(f"Name: {dictionary['name']}, Email: {dictionary['email']}")
    
    def check_total_bank_balance(self):
        return self.bank.total_balance
    
    def check_total_loan_amount(self):
        return self.bank.total_loan_balance
    
    def on_off_loadn_features(self, is_opnen):
        if is_opnen == 0:
            return False
        elif(is_opnen == 1):
            return True
        else:
            print("Wrong choice!!!")

            
    
    