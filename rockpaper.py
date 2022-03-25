import random
#if i wanted to ask a player if they wanted to play another round, i would play a wild loop below
#thoughi i would make sure afterward to have a break in the end to stop the loop and indent the lines below
while True:
    choices = ["rock", "paper", "scissors"]
# make sure for my inputs to include .lower() so i am able type in all caps or uppercase
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

#copy and pasted elif and 2 if statements down until each one had different elif statements of rock, paper, scissors
    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
