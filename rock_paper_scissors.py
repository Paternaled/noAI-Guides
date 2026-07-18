import random

options = ["Rock", "Paper", "Scissors"]

number = random.randint(0, 2)
opponent_choice = options[number]
player_input = int(input("Rock, Paper, or Scissors? \nType 0, 1, or 2 respectively.\n"))
player_choice = options[player_input]
if opponent_choice == player_choice:
    print("Draw!")
elif opponent_choice == options[0] and player_choice == options[1]:
    print("You win!")
elif opponent_choice == options[0] and player_choice == options[2]:
    print("You lose!")
elif opponent_choice == options[1] and player_choice == options[0]:
    print("You lose!")
elif opponent_choice == options[1] and player_choice == options[2]:
    print("You win!")
elif opponent_choice == options[2] and player_choice == options[1]:
    print("You lose!")
elif opponent_choice == options[2] and player_choice == options[0]:
    print("You win!")
else:
    print("Something's wrong!")
