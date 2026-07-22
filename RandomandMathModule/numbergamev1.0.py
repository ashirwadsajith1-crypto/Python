import random
number=random.randint(0,9)
print("Hello Champ🏆. I am going to think a number between 0 and 9. You have to guess it and ou have unlimited tries. Good luck :) ")
while True:
     guess=int(input("Give me your guess: "))
     if number==guess:
          print(f"Congratulations!!! You have guessed my number. The number is {number}")
          break
     else:
        print("Oops!!! That wasn't right try again")
