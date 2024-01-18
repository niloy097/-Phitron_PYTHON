from bank import Bank
from user import User, Admin
def main():
    rupali = Bank("Rupali Bank Limited")
    # Admins
    niloy = Admin(rupali, "Naeem Biswass Niloy", "niloybiwass097@gmail.com", 'x122')
    niloy.create_an_account(324)
    rakib = Admin(rupali, "Khandakar", "x@y.com", '232a/b')
    rakib.create_an_account(2342)

    # usrs
    kamal = User(rupali, "Kamal Hossen", "kamal@gmail.com", "Gulshan")
    kamal.create_an_account(234, "savings")
    
    jamal = User(rupali, "Jamal Hossen", "Jamal@gmail.com", "Gulshan")
    jamal.create_an_account(234, "savings")
    
    kamal.deposit_money(100)
    kamal.check_transaction_history()
    print("Current balance: ", kamal.check_current_balance())
    print("Bank Balance", niloy.check_total_bank_balance())
    print()
    kamal.withdraw_amount(10)
    kamal.check_transaction_history()
    print("Current balance: ", kamal.check_current_balance())
    print("Bank Balance", niloy.check_total_bank_balance())
    
    kamal.take_loan(500, niloy.on_off_loadn_features(True))
    kamal.take_loan(100, niloy.on_off_loadn_features(False))
    print("Current balance: ", kamal.check_current_balance())
    print("Total Loan given: ",niloy.check_total_loan_amount())
    
    niloy.view_all_user_list()
    niloy.view_all_admin_list()
    
    
    
if __name__ == '__main__':
    main()