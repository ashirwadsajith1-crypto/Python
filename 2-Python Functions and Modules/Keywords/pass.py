# Write a program to satisfy the following conditions of the given range: If the number is divisible by 20, it provides an output "twist." If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.” If the number is divisible by 3, it will give an output "buzz." Otherwise, it will give the output of that number.
num1=int(input("Enter the number: "))
if num1 %20==0:
    print("Twist!!!")
elif num1 %15==0:
    pass
elif num1%5==0:
    print("Fizz🥫")
elif num1%3==0:
    print("Buzz🐝")
else:
    print(num1)