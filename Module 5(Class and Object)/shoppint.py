class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
        
    def add_to_cart(self, item, price, quantity):
        self.product = {"item" : item, "price" : price, "quantity" : quantity}
        self.cart.append(self.product)
        
    def chekcout(self, amout):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print("Total taka dite hobe", total)
        if(amout < total):
            print(f"Please provide {total - amout} more")
        else:
            extra = amout - total
            print(f"Here is your items and extra money {extra}")
    def remove_item(self, item):
        get_idx = -1
        for ele in self.cart:
            if ele["item"] == item:
                get_idx += 1
                break
            else:
                get_idx += 1
        self.cart.remove(self.cart[get_idx])
        print(f"The {item} was removed form the list")
        
        
swapan = Shopping("Alan Swapan")
swapan.add_to_cart("Alu", 50, 6)
swapan.add_to_cart("Dim", 12, 24)
swapan.add_to_cart("Rice", 50, 5)

print(swapan.cart)

swapan.remove_item("Alu")

print(swapan.cart)
# swapan.chekcout(1600)