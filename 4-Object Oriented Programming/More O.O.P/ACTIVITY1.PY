class Vehicle:
    def __init__(self):
       print("This is a constructor.")
    def display(self):
        print("This is the display function")
    def new_vehicle(self):
        print("This is a new vehicle function method")
obj1=Vehicle()
obj2=Vehicle()
obj1.display() 
obj2.display()
obj1.new_vehicle() 
obj2.new_vehicle()
         