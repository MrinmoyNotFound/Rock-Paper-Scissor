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
  play_again = str(input("Do you want to play again? Type yes/no ")).lower()


  if play_again == 'yes':
    print("Ok") 
  else:
    play_again == 'no'
    print("As you wish, bye. ")
    break


#Codes end here
		