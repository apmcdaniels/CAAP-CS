# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 5
	board = []

	def __init__(self):
		for i in range(self.size):
			name = 'Player ' + str(i) + ': '
			moves = 5
			score = Score(name, moves)
			self.board.append(score)

	# prints the leaderboard
	def print_board(self):
		print("The Leaderboard:\n")
		for i in range(self.size):
			score = self.board[i]
			pname = score.get_name()
			pscore = score.get_score()
			print(pname, pscore)


	# checks if given score should be in the leaderboard
	def update(self, score):
		for i in range(self.size):
			if pscore < self.board[-1].get_score():
				insert_score(self, score)
				board.pop(-1)
			return

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score, i):
		for i in range(self.size):
			if score.get_score() < self.board[i].get_score():
				board.insert(i,score)
			return


#checking our score againat the last one to see a if we should be in the
#append addsc on to the end of the list
#function called insert for the leaderboard
#it takes in an index and an element (which is the score) then it will insert the element that you pass at the index that you pass
#use a loop to go through scores etc.
#reference the calender problem for this
#board [i] in your loop will help you to access the ith element
#board[i].score
