#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

logo = art.logo
print(logo)
print("Welcome to the number guessing game!")

number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if (difficulty == 'easy'):
  attempts = 10
else:
  attempts = 5

while (attempts > 0):
  print(f"You have {attempts} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))
  if (guess == number):
    print("This is the number!")
    break
  elif (guess > number):
    print("Too High")
  else:
    print("Too Low")

  attempts -= 1