#	Description:	Various menu functions to allow the user to
#					access the database and choose operations for
#					getting desired information about players.

from statFunctions import *

# String for the main menu options.
mainMenuPrompt = """\
------------------------------------------------
[1] Search for a player.
[2] Open history options.
[Q] Quit.
------------------------------------------------
Select: """

# String for the "[1] Search for a player" menu options.
playerMenuPrompt = """\
------------------------------------------------
	[1] View stats.
	[2] View info.
	[B] Back.
------------------------------------------------
Select: """

# String for the "[2] Open history options" menu options.
historyMenuPrompt = """\
------------------------------------------------
	[1] Compare 2 players.
	[2] View search history.
	[3] Remove a search.
	[4] Clear search history.
	[B] Back.
------------------------------------------------
Select: """
#______________________________________________________________________________

# Takes in user selection for the main menu and calls the appropriate
# function or error messages.
def mainMenuSelect(prompt, player, history):
	select = input(prompt)

	if select == '1':
		try:
			player = searchPlayer()
			history.append(player)
			print(green+f"{player.firstname} {player.lastname} added to history.", white)
			while True:
				if playerMenuSelect(playerMenuPrompt, player, history):
					break
		except IndexError:
			print(red+"ERROR:", white+"Player not found.")
	elif select == '2':
		while True:
			if historyMenuSelect(historyMenuPrompt, history):
				break
	elif select == 'Q' or select == 'q':
		print("\nThank you for using the NBA Stats Database!\n")
		quit()
	else:
		print(red+"ERROR:", white+"Invalid input, please try again.")

# Takes in user selection for the player menu and calls the appropriate
# function or error messages.
def playerMenuSelect(prompt, player, history):
	select = input(prompt)

	if select == '1':
		printStats(player)
	elif select == '2':
		printInfo(player)
	elif select == 'B' or select == 'b':
		return True		# break loop
	else:
		print(red+"ERROR:", white+"Invalid input, please try again.")
	return False	# keep looping
	
# Takes in user selection for the history menu and calls the appropriate
# function or error messages.
def historyMenuSelect(prompt, history):
	select = input(prompt)

	if select == '1':
		if len(history) >= 2:
			comparePlayers(history)
		else:
			print(red+"ERROR:", white+"Need 2+ players for comparison.")
	elif select == '2':
		if len(history) > 0:
			printSearchHistory(history)
		else:
			print(red+"ERROR:", white+"No history.")
	elif select == '3':
		if len(history) > 0:
			if removeSearch(history):
				print(green+"Search successfully removed."+white) 
			else:
				print(red+"ERROR:", white+"Name was not found in history.")
		else:
			print(red+"ERROR:", white+"No history.")
	elif select == '4':
		if len(history) > 0:
			history.clear()
			print(green+"Search history successfully cleared."+white)
		else:
			print(red+"ERROR:", white+"No history to remove.")
	elif select == 'B' or select == 'b':
		return True		# break loop
	else:
		print(red+"ERROR:", white+"Invalid input, please try again.")
	return False	# keep looping
