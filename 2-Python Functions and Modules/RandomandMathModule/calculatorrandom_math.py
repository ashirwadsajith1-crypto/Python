import random
import math
a=random.randint(1,10)
funchoices=["Cricket", "Singing", "Piano", "Basketball", "Badminton"]
random_activity=random.choice(funchoices)
number=random.randint(1,5)
print("Hello Champ🏆. I am going to think a number between 0 and 9. You have to guess it and ou have unlimited tries. Good luck :) ")
while True:
     guess=int(input("Give me your guess: "))
     if number==guess:
          print(f"Congratulations!!! You have guessed my number. The number is {number}")
          break
     else:
        print("Oops!!! That wasn't right try again")
decimal_no=float(input("Enter a decimal number: "))
round_up=math.ceil(decimal_no)
round_down=math.floor(decimal_no)
first_number=int(input("Enter the first number: "))
second_number=int(input("Enter the second number: "))
hcf=math.gcd(first_number,second_number)
print(f"The round up decimal number is {round_up} and the rounded down decimal number is {round_down}. The greatest common divisor is {hcf}.")

