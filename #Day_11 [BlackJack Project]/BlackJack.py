## code
## import game logo
import random
import art

logo = art.logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  ## 13 cards

## special cards
ace   = cards[0]

def CalcScore(in0, in1):
  return in0 + in1

def getCards():
  return cards[random.randint(0, 12)]

def newCard(score):
  card = cards[random.randint(0, 12)]
  if (card == ace):
    if ((score + ace) > 21):
      card = 1
    else:
      card = 11

  return card

def printResult (userCards,computerCards,userScore,computerScore,res):
  print(f"Your final hand: {userCards}, final score: {userScore}")
  print(f"Computer's final hand: {computerCards}, final score: {computerScore}")
  if (res == "win"):
    print("You Win")
  elif (res == "winOver"):
    print("Opponent went over, you win")
  elif (res == "lose"):
    print("You lose")
  else:
    print("Draw")


gameOver = False

while (gameOver == False):

  keepGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if (keepGame == 'n'):
    break

  print(logo)
  userFirstCard  = getCards()
  userSecondCard = getCards()

  computerFirstCard  = getCards()
  computerSecondCard = getCards()

  userCards     = [userFirstCard, userSecondCard]
  computerCards = [computerFirstCard,computerSecondCard]

  userScore     = CalcScore(userFirstCard, userSecondCard)
  computerScore = CalcScore(computerFirstCard, computerSecondCard)

  print(f"Your Cards: {userCards}, current score: {userScore}")
  print(f"Computer's first card: {computerFirstCard}")

  pullCard = True

  while (pullCard == True):

    getNewCard = input("type 'y' to get another card, type 'n' to pass: ")

    if (getNewCard == 'y'):
      ## the user takes a new card
      getUserCard  = newCard(userScore)
      userScore += getUserCard
      userCards.append(getUserCard)

      if (userScore > 21):
        print(f"Your cards: {userCards}, current Score: {userScore}")
        print(f"Computer's first card: {computerFirstCard}")
        print(f"Your final hand: {userCards}, final score: {userScore}")
        print(f"Computer's final hand: {computerCards}, final score: {computerScore}")
        print("You went over, you lose")
        pullCard =  False

      ## if the user not busted
      else:
        print(f"Your cards: {userCards}, current Score: {userScore}")
        print(f"Computer's first card: {computerFirstCard}")
          
    else:
        pullCard = False

        if (computerScore < 17):
          while (computerScore < 17):
            getComputerCard  = newCard(computerScore)
            computerScore += getComputerCard
            computerCards.append(getComputerCard)

          if (computerScore > 21):
            printResult(userCards,computerCards,userScore,computerScore,"winOver")

          elif (computerScore > userScore):
            printResult(userCards,computerCards,userScore,computerScore,"lose")

          elif (computerScore < userScore):
            printResult(userCards,computerCards,userScore,computerScore,"win")

          else:
            printResult(userCards,computerCards,userScore,computerScore,"draw")

        else:

          if (computerScore > userScore):
            printResult(userCards,computerCards,userScore,computerScore,"lose")

          elif (computerScore < userScore):
            printResult(userCards,computerCards,userScore,computerScore,"win")

          else:
            printResult(userCards,computerCards,userScore,computerScore,"draw")

  
print("Game's Over!")