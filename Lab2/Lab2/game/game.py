# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ''
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	score = Score(name, moves)
	if won:
		leaderboard.update(score)
	print ("\nGame Over.")
	name = ''
	moves = 0
	leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name
		global moves
		print("Welcome to The Program.  This Program is running from an AI chip that was inserted\ninto your arm by the Hostile Political Party as a means of maintaining control.")
		print(" ")
		print("Because you committed a small infraction, this Program was initiated\nas a way to eliminate you.  In the Program, you'll be transported through a series of scenarios.")
		print(" ")
		print ("In each of the scenarios, you will be faced with a series of tasks which you will have to complete.\nYour goal is to complete all the tasks so that you can terminate the Program and reclaim your livelihood!\nTo quit enter :q at any time. You will have 5 lives.\nHope you will make it!")
		print("*****************************************************************")
		name = input("\nLet's play. Enter your name. > ")
		if (name == ':q'):
			exit(1)
		a_map = Map('treehouse_jungle')
		a_game = Engine(a_map)
		moves = a_game.play()
		game_over(a_game.won())

play_game()
