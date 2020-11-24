from gameComponents import gameVars

def winorlose(status): 
	
	if status == "won":
		pre_message = "Winner, winnner, chicken dinner!"
	else:
		pre_message = "Loser."

	print(pre_message + "Would you like to play again?")

	choice = input("Y / N")

	if choice == "Y" or choice == "y":

		# reset the game and start over
		gameVars.user_lives = 5
		gameVars.computer_lives = 5
		gameVars.user_choice = False

	elif choice == "N" or choice == "n":
		# exit message and quit
		print("you chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice - Y or N")
		choice = input("Y / N")
