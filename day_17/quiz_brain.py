# asking the questions
# check if the answerr is correct
# check if the were the end of the quiz
class Quizbrain:
    
  
    def __init__(self,q_list):
        self.question_number=0
        self.questions_list = q_list 
        self.score=0

    def still_has_question(self):
        return self.question_number<(len(self.questions_list ))
    



    def next_question(self):
        current_question=self.questions_list[self.question_number]
        self.question_number += 1
        user_answer=input(f'Q.{self.question_number}:{current_question.text} (True/False)')
        score=self.check_answer(user_answer,current_question.answer)
        print(f"Your current score is:({score}/{self.question_number})")

    
    def check_answer(self,user_answer,correct_answer):
        if correct_answer.lower()==user_answer.lower():
            self.score+=1
            print('You got it!')
        else:
            print("That's wrong")
        print(f"The correct is {correct_answer}.")
        print("\n")
        return self.score 
    

    



