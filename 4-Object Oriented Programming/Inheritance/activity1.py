class Family:
    def __init__(self,eye_color,height_in_cm):
        self.eye_color=eye_color
        self.height_in_cm=height_in_cm
        print("This is the constructor of parent class")
    def show_traits(self):
        print(f"Eye color= {self.eye_color} and Height(in cm)= {self.height_in_cm} ")
        
class Child(Family):
    def __init__(self,name,age,eye_color,height_in_cm):
        self.name=name
        self.age=age
        super().__init__(eye_color, height_in_cm)
        print("This is the constructor of child class")
    def show_traits(self):
            super().show_traits()
            print(self.name,self.age)
obj1=Family("Black",157)
obj2=Child("Joe_Mama",25,"Green",167)
obj1.show_traits()
obj2.show_traits()
print(obj1)
print(obj2)