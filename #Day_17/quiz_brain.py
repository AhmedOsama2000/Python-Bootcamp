class  QuizBrain:

    def __init__(self, question_list, question_number=0, score=0):
        self.question_number = question_number
        self.question_list = question_list
        self.score = score

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        user_answer = input(f"Q.{self.question_number + 1} {current_question} True/False: ").title()
        correct_answer = self.question_list[self.question_number].answer

        self.check_answer(user_answer, correct_answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong")

        print("The correct answer was: " + self.question_list[self.question_number].answer + ".")
        print("Your current score is: " + str(self.score) + "/" + str(self.question_number + 1))






