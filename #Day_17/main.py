# Quiz Game
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:

    text = question["text"]
    answer = question["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():

    quiz_brain.next_question()

#     if answer == random_question.answer:
#         print("You got it right!")
#         score += 1
#
#     else:
#         print("That's wrong")
#
#     print("The correct answer was: " + random_question.answer + ".")
#     print("Your current score is: " + str(score) + "/" + str(question_number + 1))
#     question_bank.pop()
#     question_number += 1
#
print("You've completed the quiz")
print("Your final score was: " + str(quiz_brain.score))
