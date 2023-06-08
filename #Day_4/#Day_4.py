#Day_4
## Python use something called Mersenne Twister in randomization
## to using the randmozation function we should use import random "module
import random # => import the module
import my_module

rand_int = random.randint(1,10)
print(rand_int)

rand_float = random.random() # ==> from 0.0 to 1.0
print(rand_float)

## To access a variable in external file use the . operator method
print(my_module.external_var)

# Python Lists
# combination of elements of any data type
# index start from  0 , -ve numbers starts indexing from the end of the list
# a list element can be overwritten by assigning new data into the element using its index
# append methos is used to add a new item to the list
# extend methos is used to add a new item or more to the list
# lists can be nested (use a list as an element inside an another list)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[-1])
print(states_of_america[0])

states_of_america[0] = "Dellware"
states_of_america.append("temp_state") # ==> added in the end of the list

