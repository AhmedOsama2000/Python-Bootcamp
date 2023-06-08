# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
## random importion
import random
player_choice = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)
game_set        = ["Rock","Paper","Scissors"]

print(f"computer choice is {game_set[computer_choice]}")
if (player_choice == 0 and computer_choice == 1):
    print("You Lose")
elif (player_choice == 0 and computer_choice == 2):
    print("You Win")
elif (player_choice == 1 and computer_choice == 1):
    print("You Win")
elif (player_choice == 1 and computer_choice == 2):
    print("You Lose")
elif (player_choice == 2 and computer_choice == 0):
    print("You Lose")
elif (player_choice == 2 and computer_choice == 1):
    print("You Win")
else:
    print("Draw")

