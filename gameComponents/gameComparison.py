from gameComponents import gameVars
from random import randint
# # this will be the AI choice -> a random pick from the choices array
# 	computer_choice = gameVars.choices[randint(0, 2)]

# 	# just validating that I can make a choice
# 	# print outputs whatever is inside the brackets
# 	# check to see what the user input
# 	print("user chose: " + gameVars.user_choice)

# 	# validate that the random choice worked for the AI
# 	print("AI chose: " + computer_choice)

def comparison(user_choice):

	# this will be the AI choice -> a random pick from the choices array
	computer_choice = gameVars.choices[randint(0, 2)]

	# just validating that I can make a choice
	# print outputs whatever is inside the brackets
	# check to see what the user input
	print("user chose: " + gameVars.user_choice)

	# validate that the random choice worked for the AI
	print("AI chose: " + computer_choice)

	if (computer_choice == gameVars.user_choice):
		print("tie")

	elif (computer_choice == "rock"):
		if (gameVars.user_choice == "scissors"):
			gameVars.user_lives -= 1
			print("You lose! player lives:", gameVars.user_lives)
		else:
			print("""
				     _______
				---'    ____)____
           				   ______)
         				  _______)
         				 _______)
				---.__________) You win! 
				""")
			gameVars.computer_lives -= 1

	elif (computer_choice == "paper"):
		if (gameVars.user_choice == "scissors"):
			print("""
    			    	   _______
				---'   ____)____
          				  ______)
       					__________)
      				  	(____)
				---.__(___) You win!
				""")
			gameVars.computer_lives -= 1
		else:
			gameVars.user_lives -= 1
			print("You lose! player lives:", gameVars.user_lives)

	elif (computer_choice == "scissors"):
		if (gameVars.user_choice == "paper"):
			gameVars.user_lives -= 1
			print("You lose! player lives:", gameVars.user_lives)
		else:
			print("""
				      _______
				  ---'   ____)
     					(_____)
      					(_____)
      					(____)
				  ---.__(___) You win! 
				""")
			gameVars.computer_lives -= 1
