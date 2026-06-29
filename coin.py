"""
Name of program: coin.py
Author: Jonathan Dotse
Purpose: This program defines the coin class used in a match coin game
Date: June 28, 2026
"""

import random  

class Coin:
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup ='Tails'


    def get_sideup(self):
        return self.__sideup