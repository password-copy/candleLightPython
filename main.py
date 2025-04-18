from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    # newQ = QuestionModel(question_data[i]["text"],question_data[i]["answer"])
    newQ = QuestionModel(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(newQ)
    # print(i)
    # print(question_data[i]["text"])
    # print(question_data[i]["answer"])
    # print(newQ.question)
    # print(newQ.answer)
    # print("----------")
#
newQuiz = QuizBrain(question_bank)

while newQuiz.still_has_questions():
    newQuiz.nextquestion()
print("You have completed the quiz!")
print(f"Your final score is {newQuiz.score}/{newQuiz.question_number}")



#newQuiz.nextquestion()
# print(question_bank[0].question)


