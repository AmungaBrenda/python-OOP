class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, name, color, max_speed):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0
    
    def move(self):
        """Base movement method - to be overridden by subclasses"""
        return f"{self.name} is moving somehow."
    
    def stop(self):
        """Stop the vehicle"""
        self.current_speed = 0
        return f"{self.name} has stopped."
    
    def get_info(self):
        """Return information about the vehicle"""
        return f"{self.color} {self.name}, Max Speed: {self.max_speed} km/h, Current Speed: {self.current_speed} km/h"


class Car(Vehicle):
    """Car class representing land vehicles with wheels"""
    
    def __init__(self, name, color, max_speed, num_wheels=4):
        super().__init__(name, color, max_speed)
        self.num_wheels = num_wheels
        self.terrain = "land"
    
    def move(self):
        """Override move method for cars"""
        self.current_speed = min(self.max_speed, 60)
        return f"🚗 {self.name} is driving on {self.num_wheels} wheels at {self.current_speed} km/h."
    
    def honk(self):
        """Car-specific method"""
        return f"🔊 {self.name} honks: BEEP BEEP!"


class Boat(Vehicle):
    """Boat class representing water vehicles"""
    
    def __init__(self, name, color, max_speed, boat_type):
        super().__init__(name, color, max_speed)
        self.boat_type = boat_type
        self.terrain = "water"
    
    def move(self):
        """Override move method for boats"""
        self.current_speed = min(self.max_speed, 30)
        return f"🚢 {self.name} is sailing on water at {self.current_speed} km/h."
    
    def anchor(self):
        """Boat-specific method"""
        return f"⚓ {self.name} has dropped anchor."


class Plane(Vehicle):
    """Plane class representing air vehicles"""
    
    def __init__(self, name, color, max_speed, max_altitude):
        super().__init__(name, color, max_speed)
        self.max_altitude = max_altitude  # in feet
        self.current_altitude = 0
        self.terrain = "air"
    
    def move(self):
        """Override move method for planes"""
        self.current_speed = min(self.max_speed, 800)
        self.current_altitude = 30000  # cruising altitude
        return f"✈️ {self.name} is flying through the air at {self.current_speed} km/h at altitude {self.current_altitude} feet."
    
    def land(self):
        """Plane-specific method"""
        self.current_altitude = 0
        self.current_speed = 0
        return f"🛬 {self.name} has landed safely."


class Submarine(Vehicle):
    """Submarine class representing underwater vehicles"""
    
    def __init__(self, name, color, max_speed, max_depth):
        super().__init__(name, color, max_speed)
        self.max_depth = max_depth  # in meters
        self.current_depth = 0
        self.terrain = "underwater"
    
    def move(self):
        """Override move method for submarines"""
        self.current_speed = min(self.max_speed, 40)
        self.current_depth = 100  # meters below surface
        return f"🌊 {self.name} is submerging underwater at {self.current_speed} km/h at depth {self.current_depth} meters."
    
    def surface(self):
        """Submarine-specific method"""
        self.current_depth = 0
        return f"🔝 {self.name} has surfaced."


def demonstrate_movement(vehicles):
    """Demonstrate polymorphic behavior with multiple vehicles"""
    print("\n=== Vehicle Movement Demonstration ===")
    for vehicle in vehicles:
        print(f"\n{vehicle.get_info()}")
        print(vehicle.move())
    print("\n=== End of Demonstration ===")


# Create instances of different vehicles
sedan = Car("Toyota Camry", "Blue", 180)
speedboat = Boat("Sea Ray", "White", 70, "Speedboat")
airliner = Plane("Boeing 747", "White", 920, 43000)
deep_sea = Submarine("Nautilus", "Black", 50, 500)

# Store all vehicles in a list to demonstrate polymorphism
vehicles = [sedan, speedboat, airliner, deep_sea]

# Demonstrate polymorphic behavior
demonstrate_movement(vehicles)

# Demonstrate type-specific methods
print("\n=== Vehicle-Specific Actions ===")
print(sedan.honk())
print(speedboat.anchor())
print(airliner.land())
print(deep_sea.surface())