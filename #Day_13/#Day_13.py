############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): ## this is the bug, range counts until N - 1, so 20 does't taken
    ## correct code is range(0,21)
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) ## here's the bug, last index of the list is 5 
# # correct code is randint(0,5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
## but if the input's 1994 exactly, you have to change one of the conditions

# # Fix the Errors
# age = input("How old are you?") ## this should be casted to int
# if age > 18:
# print("You can drive at age {age}.") ## f"" should be added because age is a variable

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) ## you'll made its value 0(false) or 1(true) because of ==
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) ## the last item only is the one that got appended , just indent it wihing the for loop
#   print(b_list)

# mutate([1,2,3,5,8,13])