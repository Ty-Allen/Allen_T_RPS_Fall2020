# import packages to extend python
from random import randint

# [] => this is an array. An array is a special type of container that can hold multiple items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock","paper", "scissors"]

# this is the player choice
user_choice = input("choose rock, paper or scissors: ")

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
		print("you lose!")
	else:
		print("you win!")

elif (computer_choice == "paper"):
	if (user_choice == "scissors"):
		print("you win!")
	else:
		print("you lose!")

elif (computer_choice == "scissors"):
	if (user_choice == "paper"):
		print("you lose!")
	else:
		print("you win!")
