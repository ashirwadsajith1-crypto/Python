import random
 
def rps():
    '''Play a game of rock, paper, or scissors.'''
    choices = ["rock", "paper", "scissors"]
    
    while True:
         
        user_choice = input("\nLet's play rock paper scissors. Make your choice (all lowercase): ").strip()
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice! Please type rock, paper, or scissors.")
            continue
            
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
         
        if computer_choice == user_choice:
            print("Oh it's a draw, let's play again!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!!!")

 
if __name__ == "__main__":
    rps()
