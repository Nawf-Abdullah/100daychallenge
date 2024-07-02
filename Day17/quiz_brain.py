

class QuizBrain:
	def __init__(self,question_list):
		self.question_number=0
		self.question_list= question_list
		self.score = 0

	def still_has_question(self):
		if self.question_number<len(self.question_list)-2:
			return True
		else:
			return False


	def next_question(self):
		ans = input(f"Q{self.question_number+1}:{self.question_list[self.question_number].text}")
		if ans.lower() == self.question_list[self.question_number].answer.lower():
			print("you are crct")
			self.score+=1
		else:
			print("Wrong")

		print(f"your score is {self.score}/{self.question_number+1}")
		self.question_number+=1