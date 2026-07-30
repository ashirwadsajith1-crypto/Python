try:
    age=int(input("Enter the age: "))
    if age %2==0:
        print("Age is even")
    elif age%2==1:
        print("Age is odd")
    else:
        print("Something went wrong")
except ValueError as io:
    print(io,"I need an integer")

