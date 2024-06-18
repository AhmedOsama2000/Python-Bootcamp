import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.
def add_info (name,bid):
  bed_dict[name] = bid

def get_max(dict):
  max_bid = 0
  winner = ""
  for key in dict:
    if dict[key] > max_bid:
      max_bid = dict[key]
      winner  = key

  print(f"The winner is {winner} with a bid of ${max_bid}.")

logo = art.logo
print(logo)

bed_dict = {}

is_finished = False

while is_finished is False:
  name = input("What's your name?: ")
  bid  = int(input("What's your bid?:$"))
  add_info(name,bid)

  contn = input("Are there any other bidders? Types 'Yes' or 'no'.\n").lower()
  if contn == "no":
    is_finished = True
    
  clear()

get_max(bed_dict)
    


