#	Description:	Main executable program that prompts the user with
#					menu options to search for a player within a database.

from menuFunctions import *

player = myPlayer()		# Hold player information.
history = list()		# Hold search history.

print("\n**********************************")
print("Welcome to the NBA Stats Database!")
print("**********************************\n")

while True:
	mainMenuSelect(mainMenuPrompt, player, history)
