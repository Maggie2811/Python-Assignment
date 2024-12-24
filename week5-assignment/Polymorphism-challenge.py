# Base class: Vehicle
class Vehicle:
    def move(self):
        print("This vehicle is moving.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Create instances of each vehicle type
vehicle = Vehicle()
car = Car()
plane = Plane()
bicycle = Bicycle()

# Demonstrating polymorphism: Each vehicle moves differently
vehicle.move()  # This will call the base class method
car.move()  # This will call the Car's move method
plane.move()  # This will call the Plane's move method
bicycle.move()  # This will call the Bicycle's move method
