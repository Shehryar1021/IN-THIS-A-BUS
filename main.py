class Vehicle:
    def __init__(self,name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle):
 pass

School_bus = Bus("SCHOOL VOLVO", 180,12)
print("VEHICLE NAME:", School_bus.name, "SPEED:" , School_bus.max_speed, "MILEAGE:" , School_bus.mileage ) 