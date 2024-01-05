class Phone:
    manufactured = "China"
    
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
    
    def send_sms(self, phone, sms):
        text = f'Sending to: {phone} {sms}'
        return text


my_ph = Phone("Kala Chan", "Oppo", 9800)
print(my_ph.owner, my_ph.brand, my_ph.price)

her_ph = Phone("She", "iPhone", 120000)
print(her_ph.owner, her_ph.brand, her_ph.price)
