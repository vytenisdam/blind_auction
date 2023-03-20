import os
from art import logo
print(logo)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

item = input("What are you selling?\n").lower()
cls()
auction = {
}
def calculate_winner():
  max_bid = 0
  winner = ""
  for bidder in auction:
    bid = auction[bidder]
    if bid > max_bid:
      max_bid = bid
      winner = bidder
  print(f"The winner is {winner} with the highest bid of - {max_bid}! Congrats on acquiring a {item}!")
last = False

while last is not True:
  print(f"Today's item for sale is - {item}!")
  name = input("What is your name?\n") 
  auction[name] = int(input("What's your bid?\n"))
  answer = input("Are there any other bidders? y/n\n")
  if answer == "n":
    last = True
    cls()
    calculate_winner()
  else: 
    cls()