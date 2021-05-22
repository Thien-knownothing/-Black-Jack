from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck = cards*4
continue_game = True

#deal a card and remove from deck  
def deal(player,deck):
  dealed = random.choice(deck)
  player.append(dealed)
  deck.remove(dealed)
  return player, deck
#calculate player score
def score(player):
  if 11 in player and sum(player)>21:
    player.remove(10)
    player.append(1)
    score = sum(player)
  else:
    score = sum(player)
  return score
#check for black jack
def blackjack(player):
  if score(player)==21 and len(player) == 2:
    return True
  else:
    return False

while continue_game:
  player = []
  dealer = []
  check_play = input("Do you want to play a black jack game?: Yes/No ")
  if check_play[0].lower() != "y":
    print("Thank for visit us!")
    break
  clear()
  print(logo)
  deal(player,deck)
  deal(player,deck)
  deal(dealer,deck)
  deal(dealer,deck)
  #show player deck and first card of dealer deck
  print(f"Your current card: {player}, your current score is:{score(player)} ")
  print(f"Dealer first card is: {dealer[0]}")
  #check player and dealer deck for black jack
  if blackjack(player):
    print(player)
    print("Player have blackjack, player win")
  elif blackjack(dealer):
    print(dealer)
    print("Dealer have blackjack, dealer win")
  else:
    while score(player) <= 21:
      get_card = input("Do you want to get one more card?: Yes/No  ")
      if get_card[0].lower() == "y":
        deal(player,deck)
      elif get_card[0].lower() == "n":
        break
      print(f"Your current card: {player}, your current score is:{score(player)} ")
    while score(dealer) < 17:
      deal(dealer,deck)
    print("-----------------------------------")
    print(f"Your final deck is: {player}, your final score is:{score(player)} ")
    print(f"Dealer deck: {dealer}, dealer score is {score(dealer)}")
    #winning condition check
    if score(player) > 21:
      print('You are Busted')
    elif score(dealer) > 21:
      print("Dealer Busted, you win")
    elif score(player) > score(dealer):
      print(f"Your score is: {score(player)}, dealer score is: {score(dealer)}, you win")
    elif score(player)<score(dealer):
      print(f"Your score is: {score(player)}, dealer score is: {score(dealer)}, dealer win")
    else:
      print("Draw")
  
