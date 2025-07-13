# class QuizBrain:
#     def __init__(self, q_list):
#         self.question_number = 0
#         self.question_list = q_list
#         self.score = 0

#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         user_response = input(
#             f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
#         self.check_answer(user_response, current_question.answer)
#         if user_response.strip().lower() == "exit":
#             return False

#         self.question_number += 1
#         return True

#     def still_has_questions(self):
#         return self.question_number < len(self.question_list)

#     # correct_answer is getting its value passed in from self.check_answer(user_response, current_question.answer).
#     # Parameters can't be named using dot notation like current_question.answer or it would cause a SyntaxError.
#     # It is getting its value passed in from: def check_answer(self, user_response, current_question.answer):
#     def check_answer(self, user_response, correct_answer):
#         if user_response.lower() == correct_answer.lower():
#             self.score += 1
#             print("You got it right!")
#         else:
#             print("That's wrong.")
#         print(f"The correct answer was: {correct_answer}.")
#         print(
#             f"Your current score is: {self.score}/{self.question_number + 1}")
#         print()


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        return current_question.text  # DO NOT use input() here!

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_response, correct_answer):
        if user_response.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False
