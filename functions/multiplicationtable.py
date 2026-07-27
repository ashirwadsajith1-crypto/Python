def mult():
    a=int(input("Enter a number: "))
    print(f"Multiplication table of {a} from 1 to 10")
    for i in range(1,11):
        product=a*i
        print(f"{a} x {i} = {product}")
mult()
