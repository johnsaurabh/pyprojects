class quiz_manager:
    def __init__(self,q_list):
        self.q_number=0
        self.q_list=q_list
        self.score=0
    def still_has_questions(self):
        #has_questions=True
        return self.q_number< len(self.q_list)

        #return has_questions
    def next_question(self):

        current_question= self.q_list[self.q_number]
        self.q_number+= 1
        user_answer=input(f"Q.{self.q_number} {current_question.q_text} True/False ")
        self.check_answer(user_answer,current_question.q_answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You got it right")
        else:
            print("Wrong answer\n")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/ {self.q_number}\n")
        print("\n")





