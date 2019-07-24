# importing random int maker module
from random import randint

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["You weren't able to terminate The Program.  You've been eliminated.",
			"Wow... All because you committed a tiny infraction!",
			"Well that wasn't very smart...",
			"Ouch!",
			"Au revoir my friend...  It's a shame you couldn't terminate The Program"
			]
	def enter(self):
		print (Death.quips[randint(0, len(self.quips)- 1)])
		return 'died'
