from abc import ABC,abstractmethod
class ABBA(ABC):
    @abstractmethod
    def display(self):
        print("Imma a diaplay function")
class abba(ABBA):
       def display(self):
            print("Imma a child class")
OBJ1=abba()
OBJ1.display()
 
   