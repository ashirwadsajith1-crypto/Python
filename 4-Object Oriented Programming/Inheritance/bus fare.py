class Vehicle:
    def __init__(self,brand,max_speed):
       self.brand=brand
       self.max_speed=max_speed
       def show_details(self):
             print(self.brand,self.max_speed)

class Car(Vehicle):
      def __init__(self,model,seats,brand, max_speed):
           self.model=model
           self.seats=seats
           super().__init__(brand, max_speed)
           def show_details(self):
                print(self.model,self.seats)  
                super.__init__(show_details)
                def fuel_type(self,fuel):
                     print(self.model,fuel)
my_car = Car("city Rider", 5, "Honda", 180)
my_car.show_details()
my_car.fuel_type("petrol")
print("Is Car a subclass of Vehicle?", 
issubclass(Car,Vehicle))