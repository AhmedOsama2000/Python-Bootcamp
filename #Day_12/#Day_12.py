################### Scope (Global VS. Local) ####################

## use 'global' keyword to inform that the used variable is a global one

enemies = 1

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

