class Phone:
    price = 12000
    color = "Blue"
    brand = "Samsung"
    features = ["Camera", "Speaker", "Hammer"]
    
    def call(self):
        print("Calling One Person")
    def send_sms(self, phon, sms):
        text = f"Sendig SMS to: {phon} and message: {sms}"
        return text

my_phone = Phone()
print(my_phone.price)
print(my_phone.color)
print(my_phone.brand)
print(my_phone.features)
my_phone.call()
print(my_phone.send_sms(42334, "I forgot to miss you"))


