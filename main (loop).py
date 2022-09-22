import msg
import random

choices = ["rock","paper","scissor"]
com_choice = random.choice(choices)
while True:
  user_choice = str(input("Choice Your Choice\nRock, Paper and Scissor : ")).lower()
#if user input is invalid or same
if com_choice == user_choice:
	print(msg.tie_msg,f"Computer choice {com_choice}")
elif user_choice not in choices:
	print(msg.invalid_input,f"Computer choice : {com_choice}")
#win function
elif user_choice == "paper":
	if com_choice == "rock":
		print(msg.win_msg,f"Computer choice : {com_choice}")
elif user_choice == "scissor":
	if com_choice == "paper":
		print(msg.win_msg,f"Computer choice : {com_choice}")
elif user_choice == "rock":
	if com_choice == "scissor":
		print(msg.win_msg,f"Computer choice : {com_choice}")
#lose function
elif user_choice == "scissor":
	if com_choice == "rock":
		print(msg.lose_msg,f"Computer choice : {com_choice}")
elif user_choice == "rock":
	if com_choice == "paper":
		print(msg.lose_msg,f"Computer choice : {com_choice}")
elif user_choice == "paper":
  if com_choice == "scissor":
	  print(msg.lose_msg,f"Computer choice : {com_choice}")
d = str(input("Do you want to play again? Type yes/no"))
d = d.lower()


"""
elif d == 'yes':
  print("Running Code Again")
  
else:
  d == 'no'
  print("Stopping Code")
  break
"""


#Codes end here
		