try:
    a=int(input("Enter the number:"))
    print(f"The number enterd is {a}")
except ValueError as ve:
    print(ve,"For the program to work, an integer is neccessary")
       