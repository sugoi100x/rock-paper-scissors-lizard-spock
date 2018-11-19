# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and return integer (0-1-2-3-4)
    """
    if(name == 'rock'):
        return 0
    elif(name == 'Spock'):
        return 1
    elif(name == 'paper'):
        return 2
    elif(name == 'lizard'):
        return 3
    elif(name == 'scissors'):
        return 4
    else:
        return "Name does not match any of the five correct input strings"

def number_to_name(number):
    """
    Take number name as input (0-1-2-3-4)
    and return string (rock-Spock-paper-lizard-scissors) 
    """
    if(number == 0):
        return 'rock'
    elif(number == 1):
        return 'Spock'
    elif(number == 2):
        return 'paper'
    elif(number == 3):
        return 'lizard'
    elif(number == 4):
        return 'scissors'
    else:
        return "Number not in correct range"

def rpsls(player_choice):
    """
    Take player_choice as input 
    and returns the result of the game 
    """
    
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Player chooses " + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice 
    
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number)%5
    
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print "Player and computer tie!"
    elif difference < 3:
        print "Computer wins!"
    else:
        print "Player wins!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")