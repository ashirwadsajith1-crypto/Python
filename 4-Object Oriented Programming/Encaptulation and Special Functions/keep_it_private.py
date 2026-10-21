class myClass:
    __privatevar=27
    def __privateMeth(self):
      print("I'm inside my class")
    def hello(self):
       print(f"The private variable value is {self.__privatevar} ")
obj1=myClass()
# obj1.__privMeth()
obj1.hello()
   
