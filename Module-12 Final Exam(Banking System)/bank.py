class Bank:
    # print("Bank Created Successfully")
    total_balance = 100000
    user_list = []
    admins = []
    transaction_history = []
    total_loan_balance = 0.0
    def __init__(self, str_name) -> None:
        self.name = str_name

