#	Description:	File accesses a public NBA API and parses data
#					to define a "myPlayer" class type. The following
#					functions convert collected data into clear
# 					information that a user can observe.

from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from myPlayer import myPlayer

#	Variables for color coding.
red = "\033[0;31;40m"
green = "\033[0;32;40m"
yellow = "\033[0;33;40m"
white = "\033[0;37;40m"

# Uses the passed first and last name of a player to perform a search
# through an NBA API. If the passed name arguments were valid, the found
# player's unique reference ID is returned as an integer.
def getPlayerID(firstname, lastname):
	playercard = players.find_players_by_full_name(f'{firstname} {lastname}')
	return playercard[0]['id']	# return id

# The searched player will have necessary data stored into the myPlayer
# class. Using the NBA API, an object is extracted containing the desired
# player's information as an accessible dictionary. The dictionary is
# then parsed to store only the necessary data into a myPlayer class type. 
def searchPlayer():
	firstname = input("[Enter player's first name]: ")
	lastname = input("[Enter player's last name]: ")

	extract = commonplayerinfo.CommonPlayerInfo(getPlayerID(firstname, lastname))
	info = extract.get_dict()['resultSets'][0]['rowSet'][0]
	stats = extract.player_headline_stats.get_dict()['data'][0]
	fullname = stats[1].split()	# Splits string into a list.

	return myPlayer(fullname[0], fullname[1], stats[2], stats[3], stats[4],
					stats[5], info[19], info[22], info[11], info[12],
					info[15], info[24], info[25])

# Outputs player statistics and the context (stat season) from
# the myPlayer class.
def printStats(plyr):
	try:
		print("------------------------------------------------")
		print(f"{'Season:':<12}{plyr.season}")
		print(f"{'PPG:':<12}{plyr.ppg}")
		print(f"{'APG:':<12}{plyr.apg}")
		print(f"{'RPG:':<12}{plyr.rpg}")
	except AttributeError:
		print(red+"ERROR:", white+"Player data is unavailable")

# Output player information from the myPlayer class.
def printInfo(plyr):
	print("------------------------------------------------")
	print(f"{'Team:':<12}{plyr.teamcity} {plyr.teamname}")
	print(f"{'Height:':<12}{plyr.height}")
	print(f"{'Weight:':<12}{plyr.weight}")
	print(f"{'Position:':<12}{plyr.position}")
	print(f"{'Career:':<12}{plyr.start}–{plyr.end}")

# Output a list of all of the players the user searched for.
def printSearchHistory(history):
	for plyr in history:
		print(f"{plyr.firstname} {plyr.lastname}")

# User may enter a player name to search through the history list
# and remove the player. Returns true if successfully deleted, false
# if player wasn't found.
def removeSearch(history):
	firstname = input("[Enter player's first name]: ")
	lastname = input("[Enter player's last name]: ")

	firstname = firstname.lower()
	lastname = lastname.lower()

	for i in range(len(history)):
		plyr_firstname = history[i].firstname.lower()
		plyr_lastname = history[i].lastname.lower()
		if f"{firstname} {lastname}" == f"{plyr_firstname} {plyr_lastname}":
			history.pop(i)
			return True
	return False

# Compares the given arguments. Color codes the larger element
# in green, smaller element in red, and equal elements in yellow.
def compareStats(plyr1_stat, plyr2_stat, stat):
	if plyr1_stat > plyr2_stat:
		print(white + f"{stat:<12}" +
			  green + f"{plyr1_stat:<23}" + red + f"{plyr2_stat}")
	elif plyr1_stat == plyr2_stat:
		print(white + f"{stat:<12}" +
			  yellow + f"{plyr1_stat:<23}{plyr2_stat}")
	else:
		print(white + f"{stat:<12}" +
			  red + f"{plyr1_stat:<23}" + green + f"{plyr2_stat}")
	print(white, end="")

# Outputs the compared (color coded) statistics for two player's
# points per game, assists per game, and rebounds per game.
def displayComparedStats(plyr1, plyr2):
	compareStats(plyr1.ppg, plyr2.ppg, "PPG:")
	compareStats(plyr1.apg, plyr2.apg, "APG:")
	compareStats(plyr1.rpg, plyr2.rpg, "RPG:")

# Takes all of the stats and information of two players and displays
# them side by side for the user.
def comparePlayers(history):
	for i in range(len(history)):
		print(f"\t[{i+1}] {history[i].firstname} {history[i].lastname}")
	print("------------------------------------------------")

	while True:
		select_plyr1 = input("Select player 1: ")
		select_plyr2 = input("Select player 2: ")
		try:
			valid_plyr1 = int(select_plyr1) >= 1 and int(select_plyr1) <= len(history)
			valid_plyr2 = int(select_plyr2) >= 1 and int(select_plyr2) <= len(history)

			if valid_plyr1 and valid_plyr2:
				break
			else:
				print(red+"ERROR:", white+"Invalid input(s), select a valid number.")
		except ValueError:
			print(red+"ERROR:", white+"Invalid input(s), select a valid number.")
	
	plyr1 = history[int(select_plyr1)-1]
	plyr2 = history[int(select_plyr2)-1]
	plyr1_name = f'{plyr1.firstname} {plyr1.lastname}'
	plyr2_name = f'{plyr2.firstname} {plyr2.lastname}'
	plyr1_team = f'{plyr1.teamcity} {plyr1.teamname}'
	plyr2_team = f'{plyr2.teamcity} {plyr2.teamname}'
	plyr1_career = f'{plyr1.start}–{plyr1.end}'
	plyr2_career = f'{plyr2.start}–{plyr2.end}'

	print("------------------------------------------------")
	print(f"{'Name:':<12}{plyr1_name:<23}{plyr2_name}")
	print(f"{'Season:':<12}{plyr1.season:<23}{plyr2.season}")
	displayComparedStats(plyr1, plyr2)
	print(f"{'Team:':<12}{plyr1_team:<23}{plyr2_team}")
	print(f"{'Height:':<12}{plyr1.height:<23}{plyr2.height}")
	print(f"{'Weight:':<12}{plyr1.weight:<23}{plyr2.weight}")
	print(f"{'Position:':<12}{plyr1.position:<23}{plyr2.position}")
	print(f"{'Career:':<12}{plyr1_career:<23}{plyr2_career}")
