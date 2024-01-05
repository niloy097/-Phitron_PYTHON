class Shop:
    cart = [] #Class Attributes
    def __init__(self, buyer):
        self.buyer = buyer
    
    def add_to_card(self, item):
        self.cart.append(item)
        

niloy = Shop("Niloy")

niloy.add_to_card("Shirt")
niloy.add_to_card("Jacket")
niloy.add_to_card("Bag")
print(niloy.cart)

shigga = Shop("Shiga")
shigga.add_to_card("Watch")
shigga.add_to_card("Cap")

print(shigga.cart)