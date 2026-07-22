import random

options = ["Rock", "Paper", "Scissors"]

def rock_paper_scissors(choice1, choice2):
    if choice1 == choice2:
        print("Draw!")
    elif choice1 == options[0] and choice2 == options[1]:
        print("You win!")
    elif choice1 == options[0] and choice2 == options[2]:
        print("You lose!")
    elif choice1 == options[1] and choice2 == options[0]:
        print("You lose!")
    elif choice1 == options[1] and choice2 == options[2]:
        print("You win!")
    elif choice1 == options[2] and choice2 == options[1]:
        print("You lose!")
    elif choice1 == options[2] and choice2 == options[0]:
        print("You win!")
    else:
        print("Something's wrong!")

while True:
    number = random.randint(0, 2)
    opponent_choice = options[number]
    player_input = int(input("Rock, Paper, or Scissors? \nType 0, 1, or 2 respectively.\n"))
    player_choice = options[player_input]
    rock_paper_scissors(opponent_choice, player_choice)
