class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
bmw=Vehicle(240,18)
print(f"Max speed is {bmw.max_speed} and mileage is {bmw.mileage}")
ferrari=Vehicle(676,67)
print(f"Max speed is {ferrari.max_speed} and mileage is {ferrari.mileage}")
