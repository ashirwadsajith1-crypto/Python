class Comp_price:
      __maxprice=900
      def display(self):
            print(self.__maxprice)
      def update(self,price):
            self.__maxprice=price
obj1=Comp_price()
# obj1.display()
obj1.__maxprice=2000
obj1.display()
obj1.update(2000)
obj1.display()