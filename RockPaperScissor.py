import random

options=("rock", "paper", "scissor")
running=True

while running:
    computer=random.choice(options)
    player=None
    
    while player not in options:
        player=input("Enter a choice(rock,paper,scissor):").lower()
        
    print(f"Player: {player}")
    print(f"Computer: {computer}")
        
    if player=="rock" and computer=="scissor":
        print("You win")
    elif player=="paper" and computer=="rock":
        print("You win")
    elif player=="scissor" and computer=="paper":
        print("You win")
    elif player==computer:
        print("It's a tie")
    else:
        print("you lose")
     
    play_again=input("Do you want to play again(y/n):").lower()       
    if play_again!= "y":
        running= False
    
print("Thanks for playing!")
        