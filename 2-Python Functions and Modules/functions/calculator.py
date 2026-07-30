def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q  
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q
print("These are the following options")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")
choice=input("Enter your choice a/b/c/d")
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
if choice=='a':
    print(add(num1,num2))
elif choice=='b':
    print(subtract(num1,num2))
elif choice=='c':
    print(multiply(num1,num2))
elif choice=='d':
    print(divide(num1,num2))
else:
    print("Something went wrong :-(")