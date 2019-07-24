# imports random madule form library
from random import randint

# the base class for the scenes.
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene().
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class TreehouseJungle(Scene):

	name = 'treehouse_jungle'

	def enter(self):
		print ("You've found yourself in the middle of a treehouse city in the jungle.\nYour job is to reach the city's headquarters in order to retrieve the documents that will allow you to move onto the next scenario.")
		print ("The bridge that would get you to the headquarters is broken!! You have to find another way to get there.")
		options = "Which do you choose:\n(1) The easy route or\n(2) The hard route?"
		print(options)
		return self.action()


	def action(self):
		tj_player_choice = input("-->")
		if tj_player_choice == ":q":
			return self.exit_scene(tj_player_choice)
		try:
			tj_player_choice = int(tj_player_choice)
		except ValueError:
			print("you need to enter number :-p")
			return self.exit_scene(self.name)
#just an organizational break
		if int(tj_player_choice) == 1:
			print("How easy!  Hope you're good at climbing and swinging through branches.")
			tj_easy_choices = input("Do you:\n(1) Choose to swing on the biggest branches, even though they're spread out?\n(2) Choose to swing on the thinner branches that are also closer together?    ")
			if tj_easy_choices == ":q":
				return self.exit_scene(tj_easy_choices)
			try:
				tj_easy_choices = int(tj_easy_choices)
			except ValueError:
				print ("you need to enter number :-p")
				return self.exit_scene(self.name)
			if int(tj_easy_choices) == 1:
				print("Unfortunately for you, you can't jump that far from one branch to another! You fall to your death.\n")
				return 'died'
				return self.exit_scene('death')
			elif int(tj_easy_choices) == 2:
				print("Even though these branches are not too strong, you're a small person and swing easily from branch to branch.  Good thing they're close to each other!")
				print("You make it into headquarters and grab what you need to get to the next scene. Onward!")
				return self.exit_scene('crazy_beach')
		elif int(tj_player_choice) == 2:
			print("I guess you like a challenge!  It's time you utilize your rope-building abilities.")
			print("you make a long tether.  Now you have to choose how you want to use it.")
			tj_hard_choices = input("Do you:\n(1) Use it to swing from your treehouse to headquarters?\n****OR****\n(2) Use it to climb all the way down the large tree, and then up the other tree that supports the headquarters treehouse?    ")
			if tj_hard_choices == ":q":
				return self.exit_scene(tj_hard_choices)
			try:
				tj_hard_choices = int(tj_hard_choices)
			except ValueError:
				print ("you need to enter number :-p")
				return self.exit_scene(self.name)
			if int(tj_hard_choices) == 1:
				print("In a crazy stroke of luck, your rope catches onto the headquarters treehouse")
				print("You make it into headquarters and grab what you need to get to the next scene. Onward!")
				return self.exit_scene('crazy_beach')
			elif int(tj_hard_choices) == 2:
				print("Well, you must not be THAT good at making ropes, because yours broke and now you're... well...")
				return 'died'
				return self.exit_scene('death')


		return exit_scene()


	def exit_scene(self, outcome):
		return outcome

class CrazyBeach(Scene):

	name = 'crazy_beach'

	def enter(self):
		print("You’ve been transported to a sandy, tropical beach.  It would be gorgeous if not for the landmines\nwhich lay beneath the sand’s surface.  To top it off, the ocean “water” is actually acid, and it's high tide.")
		print("Your goal is to make it to the other side of the beach without triggering the landmines or being overtaken by acid high tides.\nAt the opposite end of the shore is a rock with inscriptions that will serve as your instructions to get to the next scenario.")
		cb_options = "Which will you do?\n**********\n(1) Pay close attention to any bumps in the sand and then try to run to the other end?\n(2) Grab two large stick to fashion stilts.  Try using the stilts to walk along the shoreline through the acid."
		print(cb_options)
		return self.action()

	def action(self):
		cb_player_choice = input("-->")
		if cb_player_choice == ":q":
			return self.exit_scene(cb_player_choice)
		try:
			cb_player_choice = int(cb_player_choice)
		except ValueError:
			print("you need to enter number :-p")
			return self.exit_scene(self.name)

		if int(cb_player_choice) == 1:
			print("Luckily for you, you're able to avoid every landmine in the sand!  You make it to the inscribed rock, read the instructions, and are transported to the next scenario in the program.\n")
			print("You're one step closer to terminating the program and reclaiming your life!")
			return self.exit_scene('park_bench')
		elif int(cb_player_choice) == 2:
			print("The stilts just didn't work.  Despite your perfect balance, the acid ocean burned the base of your wooden stilts.  The rest didn't end too well.")
			return 'died'
			return exit_scene('death')

		return exit_scene()


	def exit_scene(self, outcome):
		return outcome


class ParkBench(Scene):

	name = 'park_bench'

	def enter(self):
		print("Now you’re walking through a beautiful park in the middle of a city.  You hear someone calling your name and turn to see an elderly person beckoning you to sit with them.  You join them on the bench, and the elder asks if you would you like to solve a riddle.")
		print("In order to make it to the last scenario, you must solve this riddle!")
		riddle = "Here's the riddle: The Guff family lived in an area that got unbearably cold during the winter.  In the middle of February, their home’s heater broke.  They had no firewood and no alternative way to heat the house.  How did they stay warm?"
		print(riddle)
		answers = "(1) They burned down the house.\n(2) They had a maintenance person fix their heater… what else?\n(3) They stood in the corners."
		print(answers)
		return self.action()


	def action(self):
		pb_player_choice = input("-->")
		if pb_player_choice == ":q":
			return self.exit_scene(pb_player_choice)
		try:
			pb_player_choice = int(pb_player_choice)
		except ValueError:
			print("you need to enter number :-p")
			return self.exit_scene(self.name)

		if int(pb_player_choice) == 1:
			print("Well...  I don't think that would be the most effective way to keep warm.")
			return 'died'
			return exit_scene('death')
		elif int(pb_player_choice) == 2:
			print("If that was the right answer, this riddle would be WAY too easy.")
			return 'died'
			return exit_scene('death')
		elif int(pb_player_choice) == 3:
			print("How clever you are!  Corners are always 90 degrees!")
			print("And now, you're transported to the final scenario.  You're almost there!")
			return self.exit_scene('bluff_lake')

		return exit_scene()


	def exit_scene(self, outcome):
		return outcome

class BluffLake(Scene):

	name = 'bluff_lake'

	def enter(self):
		print("You’re on the Bluff Lake Reserve, one of the most beautiful places in all of California.")
		print("It’s nighttime and the moon is full.  You’re on a small island in the middle of the reserve’s lake,")
		print("and in order to get the set of instructions which will allow you to finally terminate the program and")
		print("reclaim your life, you must cross the lake and get to the shore, where, resting in the low branches of a tree is the Golden Key")
		print("There’s no apparatus which could transport you to the lake’s shoreside.  You’re going to have to rely on your athleticism… again!")
		choices = "Which do you choose:\n(1) The easy route or\n(2) The hard route?"
		print(choices)
		return self.action()


	def action(self):
		bl_player_choice = input("-->")
		if bl_player_choice == ":q":
			return self.exit_scene(bl_player_choice)
		try:
			bl_player_choice = int(bl_player_choice)
		except ValueError:
			print("you need to enter number :-p")
			return self.exit_scene(self.name)
#just an organizational break
		if int(bl_player_choice) == 1:
			print("Easy does it!  It's a good thing you were on your school's swim team for so many years.")
			bl_easy_choices = input("Do you:\n(1) Swim freestyle across the lake\n(2) Swim backstroke across the lake")
			if bl_easy_choices == ":q":
				return self.exit_scene(bl_easy_choices)
			try:
				bl_easy_choices = int(bl_easy_choices)
			except ValueError:
				print ("you need to enter number :-p")
				return self.exit_scene(self.name)
			if int(bl_easy_choices) == 1:
				print("While you were swimming freestyle, a mysterious, giant, flying creature swooped in from above, out of your view!")
				print("Its huge talons grab you out of the water...  and that's the end of your story.")
				return 'died'
				return self.exit_scene('death')
			elif int(bl_easy_choices) == 2:
				print("Because you're swimming backstroke, you're able to keep an eye on any potential hazards in the sky.  You reach the shore, run to the try, grab the key, and are transported back to the real world!  You won!")
				return self.exit_scene('finished')
		elif int(bl_player_choice) == 2:
			print("Well look at you, a challenge-seeker!  You start off by swimming backstroke to the lake's shore.")
			print("But when you emerge from the water: To your left is the tree with the Golden Key.\n********************\nAnd to your right is a very hungry-looking bear. ")
			bl_hard_choices = "Do you:\n(1) Take a breath and run as fast as you can to grab the key\n****OR****\n(2) You turn toward the bear and roar at the top of your lungs in an effort to scare it away."
			if bl_hard_choices == ":q":
				return self.exit_scene(bl_hard_choices)
			try:
				bl_hard_choices = int(bl_hard_choices)
			except ValueError:
				print ("you need to enter number :-p")
				return self.exit_scene(self.name)
			if int(bl_hard_choices) == 1:
				print("You got it just in time!  The Key heats up and you are blinded by a flash of light.  You've terminated the program.  You won!!")
				return self.exit_scene('finished')
			elif int(bl_hard_choices) == 2:
				print("Why on EARTH would you try to intimidate a hungry bear??  Psh.")
				return 'died'
				return self.exit_scene('death')

		return self.exit_scene()


	def exit_scene(self, outcome):
		return outcome
