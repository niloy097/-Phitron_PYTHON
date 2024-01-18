users = {}

def create_account(name, email, address, account_type):
        account_number = len(users) + 1
        users[account_number] = {
            'name': name, #producn_name = 'lux'
            'email': email,
            'address': address,
            'account_type': account_type,
            'balance': 0,
            'transactions': [],
            'loan_count': 0
        }
        return account_number


x = create_account("Niloy", "x@y.com", 'xhshd', 'Personal')
y = create_account("Piloy", "a@b.com", 'dfdsf', 'Personal_robot')
print(x)
print(users)
print(users[1]['address'])
'''
cat['soap']['quantity'] += 1

'''
print(y)
print(users)
print(users[2]['address'])
users[2]['address'] = 'dhaka'
print(users[2]['address'])

