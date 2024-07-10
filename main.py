from replit import clear
import art
end_of_auction = False
bidders = {}
print(art.logo)
print("Welcome to our Secret Auction!")
redo = input("Do you want to take part in the auction? Type 'yes' or 'no'\n")
if redo == "no":
  print("Goodbye!")
  quit()
while redo == "yes":
  clear()
  end_of_auction = False
  print(art.logo)
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n$"))
  bidders[name] = bid
  redo = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  clear()
  
if redo == "no":
  end_of_auction = True
  clear()
  highest_bid = max(bidders.values())
  highest_bidder = max(bidders, key=bidders.get)
  print(f"Congratulations {highest_bidder}! You won with the highest bid of ${highest_bid}.")