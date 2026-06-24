medicalcause = input("Do you have a medical cause")
if medicalcause=="y":
   print("You are allowed")
else:
   attendance=input("Enter your attendance days")
   attendance=int(attendance)
   if attendance>=75:
      print("You are allowed")
   else:
      print("You are not allowed")