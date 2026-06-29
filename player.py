"""
Name: player.py
Author: Jonathan Dotse
Purpose: Defines player class for the match coins game

"""

from coin import Coin

class Player:
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()