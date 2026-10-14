class Car:
    def __init__(self,color,name):
        print("This is a constructor ")
        self.color=color
        self.name=name
    def display(self):
        print(f"{self.color},{self.name}")

obj1=Car("Red","BMW")
obj2=Car("Blue","Nisaan")
obj1.display()
obj2.display()


