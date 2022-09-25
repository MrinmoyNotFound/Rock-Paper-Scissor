import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[35m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'


tie_msgs = [
    f"{bcolors.OKGREEN}It seems that you both have same knowledge{bcolors.ENDC}",
    f"{bcolors.OKGREEN}For me both win!!{bcolors.ENDC}",
    f"{bcolors.OKGREEN}hm... Interesting{bcolors.ENDC}"
]
winner_msg = [
    f"{bcolors.OKBLUE}You win{bcolors.ENDC}",
    f"{bcolors.OKBLUE}Congratulations, you played well!!{bcolors.ENDC}",
    f"{bcolors.OKBLUE}Can you say me how you know computer's next move?{bcolors.ENDC}"
]
loser_msg = [
    F"{bcolors.RED}Better luck next time{bcolors.ENDC}",
    f"{bcolors.RED}Hm... don't be sad ,it's a game{bcolors.ENDC}",
    f"{bcolors.RED}You are so close{bcolors.ENDC}"
]
invalid_input = [
    f"{bcolors.FAIL}It's seem that you have enter a invalid choice.\nSelect Rock/Paper/Scissor{bcolors.ENDC}"
]

tie_msg = random.choice(tie_msgs)
win_msg = random.choice(winner_msg)
lose_msg = random.choice(loser_msg)
