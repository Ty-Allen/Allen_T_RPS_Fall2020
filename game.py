# import packages to extend python
from random import randint

from gameComponents import gameVars, winLose, gameComparison

# set up our game loop
while gameVars.user_choice is False:

	# this is the player choice
	print("============*/ RPS /*==============")
	print(" Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print(" Player Lives:", gameVars.user_lives, "/", gameVars.total_lives)
	print("===========================")
	print("Choose your weapon or type quit to exit\n")
	gameVars.user_choice = input("Choose rock, paper or scissors: \n")

	# if the player chooses to quit, then don't do anything else
	# just exit the process and quit the game
	if gameVars.user_choice == "quit":
		print("You chose to quit, quitter!")
		exit()
	
	# # this will be the AI choice -> a random pick from the choices array
	# computer_choice = gameVars.choices[randint(0, 2)]

	# # just validating that I can make a choice
	# # print outputs whatever is inside the brackets
	# # check to see what the user input
	# print("user chose: " + gameVars.user_choice)

	# # validate that the random choice worked for the AI
	# print("AI chose: " + computer_choice)

	

	# if (computer_choice == gameVars.user_choice):
	# 	print("tie")

	# elif (computer_choice == "rock"):l
	# 	if (gameVars.user_choice == "scissors"):
	# 		gameVars.user_lives -= 1
	# 		print("you lose! player lives:", gameVars.user_lives)
	# 	else:
	# 		print("you win!")
	# 		gameVars.computer_lives -= 1

	# elif (computer_choice == "paper"):
	# 	if (gameVars.user_choice == "scissors"):
	# 		print("you win!")
	# 		gameVars.computer_lives -= 1
	# 	else:
	# 		gameVars.user_lives -= 1
	# 		print("you lose! player lives:", gameVars.user_lives)

	# elif (computer_choice == "scissors"):
	# 	if (gameVars.user_choice == "paper"):
	# 		gameVars.user_lives -= 1
	# 		print("you lose! player lives:", gameVars.user_lives)
	# 	else:
	# 		print("you win!")
	# 		gameVars.computer_lives -= 1

	gameComparison.comparison(gameVars.user_choice)

	# check player lives and computer lives
	if gameVars.user_lives is 0:
		winLose.winorlose("lost")

		# print("Game over, Loser! Would you like to play again?")
		# choice = input("Y / N? ")

		# if choice == "Y" or choice == "y":
		# 	# reset the game and start over
		# 	gameVars.user_lives = 5
		# 	gameVars.computer_lives = 5
		# 	gameVars.user_choice = False

		# elif choice == "N" or choice == "n":
		# 	# exit message and quit
		# 	print("you chose to quit. Better luck next time!")
		# 	exit()
		# else:
		# 	print("Make a valid choice - Y or N")
		# 	choice = input("Y / N")

	elif gameVars.computer_lives is 0:
		winLose.winorlose("won")

		# print("You won, Winner! Would you like to play again?")
		# choice = input("Y / N? ")

		# if choice == "Y" or choice == "y":
		# 	# reset the game and start over
		# 	gameVars.user_lives = 5
		# 	gameVars.computer_lives = 5
		# 	gameVars.user_choice = False

		# elif choice == "N" or choice == "n":
		# 	# exit message and quit
		# 	print("you chose to quit. Better luck next time!")
		# 	exit()
		# else:
		# 	print("Make a valid choice - Y or N")
		# 	choice = input("Y / N")

	else:
		gameVars.user_choice = False
	# computer_choice = choices[randint(0,2)]			
