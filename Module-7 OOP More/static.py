class Shopping:
    cart = [] #class attributes #static attribute
    origin = "China"
    
    
    def __init__(self, name, location):
        self.name = "Jamuna City" #instance attributes
        self.location = "Jam er majh Khane"
    
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f"Buying: {item} for price: {price} and remaining: {remaining}")
        
    @staticmethod
    def multiply(a, b):
        res =  a * b
        print(res)
    
    @classmethod
    def hudai_dekhi(self, item):
        print("Kinmu nh hudain hawa khaite acihi", item)

basundhara = Shopping("Basu en dhara", "Not popular loaction")
basundhara.purchase("Lungi", 500, 1000)
Shopping.hudai_dekhi("Lungi")

Shopping.multiply(4, 6) #static methode
# basundhara.multiply(5, 2)

        