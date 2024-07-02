from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
	new_question = Question(question["text"],question['answer'])
	question_bank.append(new_question)



quiz = QuizBrain(question_bank)
is_there = quiz.still_has_question()
while is_there:
	try:
		quiz.next_question()
	except:
		break

print("quiz completed")

print(f"Your final score is {quiz.score}/{len(question_bank)}")