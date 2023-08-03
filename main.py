from classes import Question, QuizBrain
from data import question_data

question_bank = []
for q in question_data:
    new_question = Question(q["question"], q["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
still_has_questions = quiz.still_has_questions()

while quiz.still_has_questions():
    quiz.next_question()
    quiz.still_has_questions()

print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
