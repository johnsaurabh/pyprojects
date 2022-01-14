from question_model import Question
from data import question_data
from quiz_brain import quiz_manager
question_bank=[]
for question in question_data:
    q_text= question["text"]
    q_ans= question["answer"]
    q_model=Question(q_text, q_ans)
    question_bank.append(q_model)
#print(len(new_question))
quiz=quiz_manager(question_bank)
quiz.next_question()

while quiz.still_has_questions():

    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.q_number}")

