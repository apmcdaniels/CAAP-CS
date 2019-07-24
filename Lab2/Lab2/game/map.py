# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter,
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	scenes = {'treehouse_jungle' : S.TreehouseJungle(),
				'crazy_beach' : S.CrazyBeach(),
				'park_bench' : S.ParkBench(),
				'bluff_lake' : S.BluffLake(),
				'death' : Death()
				# raise ValueError ('todo')
				}

	# initializes to a starting scene
	def __init__(self, treehouse_jungle):
		self.start_scene = treehouse_jungle

	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, crazy_beach):
		return Map.scenes.get(crazy_beach)

	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene)
