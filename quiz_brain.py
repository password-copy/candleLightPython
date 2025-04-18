class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def nextquestion(self):
        # while self.question_number < len(self.question_list):
        user_input = input(f"Q{self.question_number+1}. {self.question_list[self.question_number].question} (True/False)?: ").lower()
        right_answer = self.question_list[self.question_number].answer.lower()
        self.question_number += 1
        self.check_answer(user_input, right_answer)


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_input,right_answer ):
        if user_input == right_answer:
            print("You are right!!")
            self.score +=1
            # print(f"Your score is {self.score} / {self.question_number}")

        else:
            print("That's wrong!")
        print(f"The right answer is {right_answer}.")
        print(f"Your score is {self.score} / {self.question_number}  \n")


