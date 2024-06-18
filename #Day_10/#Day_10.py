# Function with return
# return act as a break from the function, once it's executed, then the function is over
#Functions with Outputs
#Storing output in a variable
#Return as an early exit
# Docstring in python , using """  """
""" This is a docstring, which means you can add multiple lines of string
    like thie first line
    and this second line
"""
def format_name(f_name, l_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
#or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Already used functions with outputs.
print(len(formatted_name))




