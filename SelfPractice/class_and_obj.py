# class Bike:
#     name = "Honda"
#     gear = 5

# bike1 = Bike()
# print(f"{bike1.name} {bike1.gear}")

# #access attributes and assign new values
# bike1.name = "Pulser"
# bike1.gear = 4

# print(f"New name: {bike1.name}, New Gear: {bike1.gear}")

#Methodes in class:

class Room:
    length = 0.0
    widht = 0.0
    
    def calculation(self):
        print("Area of Room: ", self.length * self.widht)

study_room = Room()

study_room.length = 10
study_room.widht = 20

study_room.calculation()