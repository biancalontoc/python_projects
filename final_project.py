import random
t = ["Rock", "Paper", "Scissors"]

computer = t[random.randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie game! Try again.")
    elif player == "Scissors":
        if computer == "Paper":
            print("Computer chose paper, you win!")
        else:
            print("Computer cut you with scissors!")
    elif player == "Rock":
        if computer == "Paper":
            print("Computer chose paper, you lose!")
        else:
            print("You win! Computer chose rock.")
    elif player == "Rock":
        if computer == "Scissors":
            print("You rock! You just beat computer's scissors!")
        else:
            print("Computer smashed you! You lose.")
    else:
        print("Invalid game. Try again.")
    player == True
    computer = t[random.randint(0,2)]