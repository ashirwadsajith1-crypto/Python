a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

try:
    choice=input("Enter your choice from add, sub, mul or div: ")
except ValueError as ve:
    print(ve,"I need a string")
try:
    if choice=="add":
       print(add(a,b))
    elif choice=="sub":
        print(sub(a,b))
    elif choice=="mul":
        print(mul(a,b))
    elif choice=="div":
        print(div(a,b))
    else:
        print("Something went wrong 😢")
except ZeroDivisionError as zde:
    print(zde,"Zero is not applicable")

 

    
 
