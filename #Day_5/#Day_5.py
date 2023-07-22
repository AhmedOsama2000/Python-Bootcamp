#Day_5
# Loops in python
# For Loops
fruits = ["Apple","Peach","Pear"]
for fruit in fruits: ## first time fruit = Apple , second time fruit  = Peach and so on
  print(fruit)
  print(fruit + " Pie")

# For Loop with range(a,b,step) step is the incremental amount (a ==> starts from 0 by default)
total = 0
for number in range(1,101): ## Last number not taken into consideration
  total += number

print(total)