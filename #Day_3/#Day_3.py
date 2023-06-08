## Day_3 
## Conditional statements
## if_elif_else
## Note that if and else should be at the same indentation level
water_level = input("Enter a number ")
if int(water_level) >= 80:
  print("Drain water")
else:
  print("Continue")

## As well as for nested if indentation should be considered
 
height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     print("Please pay $5.")
#   elif age <= 18:
#     print("Please pay 7")
#   else:
#     print("Please pay $12.")
# else:
#   print("Sorry , you have to grow taller before you can ride.")

## Logical Operators:  & == and , | == or , ! == not

bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
  elif age <= 18:
    bill = 7
  else:
    bill = 12

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if (wants_photo == "Y"):
      bill += 3
    print(f"Your bill will be {bill}")

else:
  print("Sorry , you have to grow taller before you can ride.")

## lower() ==> turn into lowercase
## upper() ==> turn into upperrcase
## count() ==> number of time a letter occurs in a string (lower or upper)