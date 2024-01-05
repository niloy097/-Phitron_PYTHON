class Calculator:
    brand = "Casio MS2342"
    def add(self, n1, n2):
        return n1 + n2
    def deduct(self, n1, n2):
        return n1 - n2
    def mul(self, n1, n2):
        return n1 * n2
    def div(self, n1, n2):
        return n1 / n2


my_cal = Calculator()
print(my_cal.brand)
print(my_cal.add(11, 11))
print(my_cal.deduct(10, 1))
print(my_cal.mul(10, 10))
print(my_cal.div(10, 5))