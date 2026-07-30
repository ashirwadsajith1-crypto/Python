try:
    num1,num2=eval(input("Enter the two numbers separated by a comma (for reference a comma is ,)"))
    c=num1/num2
    print(f"The quotient of the numbers is {c}")
except ValueError as ve:
    print(ve,"I need an integer")
except ZeroDivisionError as zde:
    print(zde,"The second number shouldn't be equal to 0")
except SyntaxError as syne:
    print(syne,"Please separate by comma")
finally:
    print("***This program is for division***")





