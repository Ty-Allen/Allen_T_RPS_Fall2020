# import packages to extend python
from random import randint

# create a variable stack
# [] => this is an array. An array is a special type of container that can hold multiple items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock","paper", "scissors"]

user_lives = 5
computer_lives = 5

total_lives = 5

user_choice = False; # True and False are Booleans - data types that can be truth-y or false-y

# define a win / lose function and refer to it in our game loop
def winorlose(status): 
	
	if status == "won":
		pre_message = "Winner, winnner, chicken dinner!"
	else:
		pre_message = "Loser."

	print(pre_message + "Would you like to play again?")

	choice = input("Y / N")

	if choice == "Y" or choice == "y":

		global user_lives
		global computer_lives
		global user_choice

		# reset the game and start over
		user_lives = 5
		computer_lives = 5
		user_choice = False

	elif choice == "N" or choice == "n":
		# exit message and quit
		print("you chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice - Y or N")
		choice = input("Y / N")

# set up our game loop
while user_choice is False:

	# this is the player choice
	print("============*/ RPS /*==============")
	print(" Computer Lives:", computer_lives, "/", total_lives)
	print(" Player Lives:", user_lives, "/", total_lives)
	print("===========================")
	print("Choose your weapon or type quit to exit\n")
	user_choice = input("choose rock, paper or scissors: \n")

	# if the player chooses to quit, then don't do anything else
	# just exit the process and quit the game
	if user_choice == "quit":
		print("You chose to quit, quitter!")
		exit()

	# this will be the AI choice -> a random pick from the choices array
	computer_choice = choices[randint(0, 2)]

	# just validating that I can make a choice
	# print outputs whatever is inside the brackets
	# check to see what the user input
	print("user chose: " + user_choice)

	# validate that the random choice worked for the AI
	print("AI chose: " + computer_choice)

	if (computer_choice == user_choice):
		print("tie")

	elif (computer_choice == "rock"):
		if (user_choice == "scissors"):
			user_lives = user_lives - 1
			print("you lose! player lives:", user_lives)
		else:
			print("you win!")
			computer_lives = computer_lives - 1

	elif (computer_choice == "paper"):
		if (user_choice == "scissors"):
			print("you win!")
			computer_lives = computer_lives - 1
		else:
			user_lives = user_lives - 1
			print("you lose! player lives:", user_lives)

	elif (computer_choice == "scissors"):
		if (user_choice == "paper"):
			user_lives = user_lives - 1
			print("you lose! player lives:", user_lives)
		else:
			print("you win!")
			computer_lives = computer_lives - 1

	# check player lives and computer lives
	if user_lives is 0:
		winorlose("lost")

		# print("Game over, Loser! Would you like to play again?")
		# choice = input("Y / N? ")

		# if choice == "Y" or choice == "y":
		# 	# reset the game and start over
		# 	user_lives = 5
		# 	computer_lives = 5
		# 	user_choice = False

		# elif choice == "N" or choice == "n":
		# 	# exit message and quit
		# 	print("you chose to quit. Better luck next time!")
		# 	exit()
		# else:
		# 	print("Make a valid choice - Y or N")
		# 	choice = input("Y / N")

	elif computer_lives is 0:
		winorlose("won")

		# print("You won, Winner! Would you like to play again?")
		# choice = input("Y / N? ")

		# if choice == "Y" or choice == "y":
		# 	# reset the game and start over
		# 	user_lives = 5
		# 	computer_lives = 5
		# 	user_choice = False

		# elif choice == "N" or choice == "n":
		# 	# exit message and quit
		# 	print("you chose to quit. Better luck next time!")
		# 	exit()
		# else:
		# 	print("Make a valid choice - Y or N")
		# 	choice = input("Y / N")

	else:
		user_choice = False
	# computer_choice = choices[randint(0,2)]			
