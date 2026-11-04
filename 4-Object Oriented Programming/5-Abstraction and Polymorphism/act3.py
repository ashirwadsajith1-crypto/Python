class India():
    def lang(self):
        print("Hindi is India's language")
    def capital(self):
        print("New DElhi is India's Capial")
class US():
    def lang(self):
            print("English is US  language")
    def capital(self):
            print("Washington DC is  US Capial")
OBJ1=India()
OBJ2=US()
for i in (OBJ1,OBJ2):
     i.capital()
     i.lang()

