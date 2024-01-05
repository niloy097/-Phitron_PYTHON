class Pen:
    manufacturer = "Bangladesh"
    def __init__(self, brand, price, height):
        self.brand = brand
        self.price = price
        self.height = height
    def intfo(self):
        print("This Class is constructed for Pen")


my_Pen = Pen("Matador", 100, 5)
my_Pen1 = Pen("Linc", 10, 5)

print(my_Pen.brand, my_Pen.price, my_Pen.height)
print(my_Pen1.brand, my_Pen1.price, my_Pen1.height)