import random
import game_data
import art

logo = art.logo
vs   = art.vs
data = game_data.data

score = 0
gameOver = False

print(logo)
while (gameOver == False):
  
  if (score == 0):
    selectA = random.choice(data)
    selectB = random.choice(data)

  else:
    selectB = random.choice(data)

  print(f"Compare A: {selectA['name']}, a {selectA['description']} , from {selectA['country']}")
  print(f"Agianst B: {selectB['name']}, a {selectB['description']} , from {selectB['country']}")

  userSelect = input("Who has more followers? Type 'A' or 'B': ")
  if (userSelect == "A"):
    if (selectA["follower_count"] > selectB["follower_count"]):
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      gameOver = True
      print(f"Sorry, that's wrong. Final score: {score}")

  else:
    if (selectB["follower_count"] > selectA["follower_count"]):
      selectA = selectB
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      gameOver = True
      print(f"Sorry, that's wrong. Final score: {score}")

print("Game Over!")