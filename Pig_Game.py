#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pig Game"""

import argparse
import random


parser = argparse.ArgumentParser(description="Num of players")
parser.add_argument('numPlayers',type=int,help='Num of players')
args = parser.parse_args()


class Players():
    """Defines players"""
    def __init__(self,name):
        self.name = name
        self.score = 0
        
def Pig_Game():
    """Set up the rules of the game and number of players"""
    players_list=[]
    number_players=args.numPlayers
        
    for i in range(int(number_players)):
        player_name=raw_input("Please enter the name of player "  +  str(i+1) + ":")
        players_list.append(Players(i))
        players_list[i].name=player_name
        
    game="Start_game"
        
    while game != "Finish":
        x=0
        while x <  (len(players_list)):
            change_player = True
            while change_player == True:
                roll_or_hold=raw_input(players_list[x].name + " Do you want to roll (r) the die or hold (h)?:")
                if  roll_or_hold == "r":
                    roll_die = random.randint(1,6)
                    if roll_die ==1:
                        print "    Roll = " + str(roll_die) + " | Sorry is next player's turn"
                        change_player = False
                    else: 
                        players_list[x].score = players_list[x].score + roll_die
                        if players_list[x].score >= 100:
                            print "    You are the winner with a total score of " + str(players_list[x].score)
                            game="Finish"
                            change_player = False
                            x=len(players_list)
                        else:
                            print "    Roll = " + str(roll_die) + " Your Total score is= " + str(players_list[x].score)
                elif roll_or_hold == "h":
                    change_player = False
                    print "Next player's turn"
                elif roll_or_hold == "f":
                    change_player = False
                    x=len(players_list)
                    game="Finish"
                    print "   bye bye"
                            
                else:
                    change_player = False
                    print "    You lost your turn.  Next time please enter a correct option: r or h"

            x=x+1    
            


def play_again():
    playagain = raw_input('Do you want to play again? (Y or N): ')
    while playagain == 'Y': 
        Pig_Game()
        playagain = raw_input('Do you want to play again? (Y or N): ')
     
    
def main():
    Pig_Game()
    play_again()
   
    
if __name__== "__main__":
  main()
   
