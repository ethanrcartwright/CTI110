#CTI 110 
#P5T3 - Random Numbers
#Ethan Cartwright
#11/16/21
# use Random
import random
#diceRoll = random.randint(1,6)

def rollD6():
  roll = random.randint(1,6)
  return roll 
def roll2d6():
  roll = random.randint(2,12)
  return roll
def headsOrTails():
  roll = random.randint(0,1)
  if roll == 0 :
    roll = "head"
  else:
    roll = "tails"
  return roll
def RPS():
  choice = random.randint(1,3)
  hand = None
  if choice == 1:
    hand = "rock"
  if choice == 2:
    hand = "paper"
  if choice == 3:
    hand = "scissors"
  return hand



def main():
  #random.seed(42)
  print("Rolling Dice...")
  for num in range(10):
    roll = rollD6()
    print(roll, end = ' ')
  print()
  #2d6
  print("Rolling Two dice...")
  for num in range(10):
    roll = roll2d6()
    print(roll, end = ' ')
  #headandtails
  print()
  print("Heads or Tails?")
  for num in range(5):
    roll = headsOrTails()
    print(roll, end = ' ')
  print()
  print("Playing Rock, Paper, Scissors...")
  for num in range(5):
    myHand = RPS() 
    yourHand = RPS()
    print("My Hand: ",myHand,"|", "Your Hand:", yourHand)



main()

