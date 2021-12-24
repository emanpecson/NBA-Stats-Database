#	Description:	Class definition for myPlayer. Includes data variables
#					for player's name, stats (w/ its context), last team,
#					physical attributes, position, and career timespan.

class myPlayer:
	def __init__(self, firstname="", lastname="", season="", ppg=0, apg=0, rpg=0,
				 teamname="", teamcity="", height="", weight="", position="",
				 start="", end=""):
		self.firstname = firstname
		self.lastname = lastname
		self.season = season
		self.ppg = ppg
		self.apg = apg
		self.rpg = rpg

		self.teamname = teamname
		self.teamcity = teamcity
		self.height = height
		self.weight = weight
		self.position = position
		self.start = start	# career start
		self.end = end		# career end (unless still present)
