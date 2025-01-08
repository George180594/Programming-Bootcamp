from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
# import random

# answer= question_data[rand]['answer']
# question= question_data[rand]['text']


# a_question= Question(question,answer)
# print(a_question.text)
question_bank=[]
for question in question_data:
    question_text= question["text"]
    question_answer= question["answer"]
    new_question= Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=Quizbrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've complete the quiz")
print(f'Your final score is {quiz.score}/{quiz.question_number}')