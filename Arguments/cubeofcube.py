def cube(number):
    cubed=number**3
    print(f"The cube is{cubed}")
number=int(input("Enter the number "))
if number%3==0:
  cube(number)
else:
   print("Number is not divisible by 3. Pls try again with a number divisible by 3 😊")
