def find_larger(a,b):
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    if num1>num2:
        print("The first number is the greater number")
    elif num2>num1:
        print("The second number is the greater number")
    elif num1==num2:
        print("Both of the numbers are equal")
    else:
        print("Something went wrong :(")
find_larger(1,2)