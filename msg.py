import random

tie_msgs = ("It seems that you both have same knowledge", "For me both win!!",
            "hm... Interesting")
winner_msg = ("You win", "Congratulations, you played well!!",
              "Can you say me how you know computer's next move?")
loser_msg = ("Better luck next time", "Hm... don't be sad ,it's a game",
             "You are so close")
invalid_input = (
    "It's seem that you have enter a invalid choice. Select Rock/Paper/Scissor"
)

tie_msg = random.choice(tie_msgs)
win_msg = random.choice(winner_msg)
lose_msg = random.choice(loser_msg)
