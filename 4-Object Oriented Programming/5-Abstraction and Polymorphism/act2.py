from abc import ABC ,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        print("This is a move function")
class Human(Animal):
     def move(self):
         print("This is inside a human(class)")
class Cat(Animal):
    def move(self):
        print("This is inside a cat class")
obj1=Human()
obj1.move()
obj2=Cat()
obj2.move()

    
