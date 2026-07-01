"""
Name: Lab9_jdotse-1.py
Purpose: Using Coin and Player classes to implement main logic of the match coins game
Author: Jonathan Dotse
Date: June, 28 2026

"""

from player import Player

def main():
    print("\n--- Coin Match Game ---")

    player1 = Player("Player 1")
    player2 = Player("Player 2")

   

    choice = input("Do you want to toss the coins? (y.n): ").lower()

    while choice == 'y':

        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            print("...It's a Match! Player 1 wins a coin.")
            player1.win_coin()
            player2.lose_coin()

        else:
            print("...No Match! Player 2 wins a coin.")

            player2.win_coin()
            player1.lose_coin()


        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        #challenge
        if player1.get_wallet() == 0 or player2.get_wallet() == 0:
            print("Game Over! A player has run out of coins.\n")
            break


        choice = input("\nDo you want to toss the coins? (y/n): ").lower()

    # Printing final score
    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 wins the game!")
    else:
        print("It's a draw!")



