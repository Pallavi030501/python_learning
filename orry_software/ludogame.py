#ludo game
import sys # used for command line
print("--------ludo game---------")
from random import randint

#print("player: ",sys.argv[1]) 
#argv: argument vector
#print(randint(1,6))
#print(randint(1,6))

if len(sys.argv)<2:
    sys.exit("Please enter player name ")
player_name=sys.argv[1];



def check_winner(player,dice):
    print("Dice:",dice)
    if dice == 6:
        print(player,"winner")
    else :
        print("better luck next time",player)

check_winner(player_name,randint(1,6))


