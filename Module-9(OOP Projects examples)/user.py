from abc import ABC, abstractclassmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    
    def add_rider(self, rider):
        self.riders.append(rider)
    
    def add_driver(self, driver):
        self.drivers.append(driver)
    def __repr__(self) -> str:
        return f"{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}"

class User(ABC):
    def __init__(self, name, email, NID) -> None:
        self.name = name
        self.email = email
        self.__id = 0
        self.__NID = NID
        self.wallent = 0
    @abstractclassmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, NID, current_location, initial_amount) -> None:
        self.current_ride = None
        self.wallent = initial_amount
        self.cur_locatin = current_location
        super().__init__(name, email, NID)
        
    def load_cash(self, amount):
        if amount > 0:
            self.wallent += amount  
    
    def update_location(self, current_location):
        self.current_ride = current_location
        
    def display_profile(self):
        print(f"Rider with name {self.name} and email: {self.email}")

    def request_ride(self, ride_sharing, destination):
        if not self.current_ride:
            print("Looking for a ride")
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_drivers(ride_request)
            print("Got the ride, yeay", ride)
            self.current_ride = ride
    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, NID, cur_location) -> None:
        super().__init__(name, email, NID)
        self.cur_location = cur_location
        self.wallent = 0
    
    def display_profile(self):
        print(f"Driver with name {self.name} and email: {self.email}")
    
    def accept_ride(self, ride):
        ride.set_driver(self)   
        

class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
    
    def set_driver(self, driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()
    
    def end_ride(self, ride, amount):
        self.end_time = datetime.now()
        self.rider.wallent -= self.estimated_fare
        self.driver.wallnet += self.estimated_fare  
        
    def __repr__(self) -> str:
        return f"Ride details. Started {self.start_location} to {self.end_location}"

class Ride_Request:
    def __init__(self, rider, cur_location, end_location) -> None:
        self.rider = rider
        self.cur_location = cur_location
        self.end_location = end_location


class Ride_Matching:
    def __init__(self, drivers):
        self.available_drivers = drivers
    
    def find_drivers(self, ride_request):
        if(len(self.available_drivers) > 0):
            #TODO: find the closest driver of the rider
            print("Looking for a driver")
            driver = self.available_drivers[0]
            ride = Ride(Ride_Request.cur_location, Ride_Request.end_location)
            driver.accept_ride(ride)
            return ride


class Vehicle(ABC):
    
    speed = {
        
        'car' : 50,
        'bike' : 60,
        'cng' : 15
        
    }
    
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'Availabe' 
        super().__init__()
    
    @abstractclassmethod
    def start_drive(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    
    def start_drive(self):
        self.status = 'Unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
        
    def start_drive(self):
        self.status = "Unavailable"
        


#check the class integration

niye_jao = Ride_Sharing("Niye jao")
sakib = Rider("Saki Khan", "sakib2024@cha.com", 134, "Mohakhali", 1200)
niye_jao.add_rider(sakib)
kala_pakhi = Driver("Kala Pakhi", 'kala@sada.com', 43543, "Gulshan-1")
niye_jao.add_driver(kala_pakhi)
print(niye_jao)
sakib.request_ride(niye_jao, "Ghughu", "Uttara")
sakib.show_current_ride()