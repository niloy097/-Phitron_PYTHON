class Product:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []
        
class Shop(Product):
    def __init__(self, name, typ) -> None:
        self.typ = typ
        super().__init__(name)

    def add_product(self, name):
        self.products.append(name)
    
    def buy_product(self, pro_name):
        if pro_name in self.products:
            print("Thanks for purchasing the product")
        else:
            print("The product is not availabe")


kamal = Shop("Liquide", 'D')
buyer = Shop("Liquide", 'D')
kamal.add_product("Milk")
kamal.add_product("Oil")
kamal.add_product("Juice")
kamal.add_product("Caramel")

kamal.buy_product("Oil")

