
# Q. Demonstrating OOP Concepts in Python


# Define a global variable
traffic_light = "Green"   

 # Define Module-level Variable
speed_limit = 60   


# inheritance

class Vehicale:  # base class
    def start_engine(self):
        message ="Engine Started"  #local variable
        print(message)

class Car(Vehicale):   # derived class
    def __init__(self, make):
        self.make = make # object variable 

    def start_engine (self):
        message = "Car engine started."   #local variable & overrides the start_engine
        print(message)

class Bike(Vehicale): # derived class
    def __init__(self, type):
        self.type = type # object variable 

    def start_engine(self):
        message = "Bike engine started."   #local variable & overrides the start_engine
        print(message)




# Create instances of Car and Bike
Car = Car("Porche")
Bike = Bike("Sport Bike")

# Demonstrate inheritance and polymorphism
vehicles = [Car, Bike]
for vehicle in vehicles:
    vehicle.start_engine() 


# Print object variables
print("Car make:", Car.make)
print("Bike type:",Bike.type)

# Accessing Global and Module Variables
print( "Traffic Light:", traffic_light)
print( "Speed Limit:", speed_limit)





