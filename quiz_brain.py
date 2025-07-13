class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        return current_question.text

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_response, correct_answer):
        if user_response.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False
