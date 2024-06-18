import art
## think about this design again using recursion
# Arithmatic functions
def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1- n2

def mul(n1,n2):
  return n1 * n2

def div(n1,n2):
  if (n2 == 0):
    return "cannot divide by 0"
  else:
    return n1/n2

logo = art.logo
print(logo)

oeprations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div,
}

is_finish = False
is_cont   = 'n'
result = 0

while is_finish is False:

  num1 = float(input("What's the first number?: ")) if is_cont == 'n' else result
  for symbol in oeprations:
    print(symbol)
  operator = input("Pick an operation: ")
  num2 = float(input("What's the second number: "))


  function = oeprations[operator]
  result = function(num1,num2)

  print(f"{num1} {operator} {num2} = {result}")
  is_cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' for new: ")
    