# List and dictionaries comprehensions
# List Comprehension: create a new list from a previous list
"""
1) List Comprehension
previous method:
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

new method: {using list comprehension}
it works on any iterable item {list, string, tuple, range}
new_list = [n+1 for n in number]

conditional list comprehension: {create a list based on a condition}
a_list = [item for item in list if condition_1]

2) Dictionary  Comprehension
new_dict = {new_key:new_value for (key, value) in dict.items()}
and we can add a condition for the expression
"""

# name = "Ahmed"
#
# name_list = [char for char in name]
# print(name_list)

# nums = range(1, 5)
# nums_list = [a_num*2 for a_num in nums]
# print(nums_list)

# names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddi"]

# names_list = [name for name in names if len(name) < 5]
# names_list = [name.upper() for name in names if len(name) > 4]
# print(names_list)

# Dictionary comprehension
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddi"]

student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

# create a dictionary from existing one
passed_students = {passed_student:score for (passed_student, score) in student_scores.items() if score > 50}
print(passed_students)