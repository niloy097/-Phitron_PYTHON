class Shop:
    shopping_mall = "Jamuna"
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] #Instance Atrributes
    def add_to_card(self, item):
        self.cart.append(item)


mhza = Shop("Mehjabin")
mhza.add_to_card("shoe")
mhza.add_to_card("Phone")

nish = Shop("Nisho")
nish.add_to_card("Hat")
nish.add_to_card("Watch")

print(mhza.cart)
print(nish.cart)