# balance = 3000

# def buy_things(item, price):
#     balance = 500
#     dream_phone = "xPhone"
#     print(f"Prev balance value:", balance)
#     # balance = balance - price
#     print(f"Balance inside the function", balance)
    
# buy_things("Sunglass", 1000)
# print(dream_phone)


balance = 3000
def buy(item, price):
    global balance
    print(balance)
    balance = balance - price
    print(item, balance)


buy("xphone", 1000)