import os
from pyfiglet import Figlet
from models.game import Game
from models.board import Board


class View:

    def __init__(self):
        self.game = Game()
        self.board = Board()

    def print_menu(self):
        f = Figlet(font="slant")
        print(f.renderText("TicTacToe"))
        print("""
        1. Player vs Player
        2. Player vs Computer
        3. Show Stats
        4. Settings
        5. Exit
            """)
        while True:
            try:
                inp = int(input("Enter your choice:...\n"))
                if inp == 1:
                    self.game.clear_terminal()
                    return inp
                elif inp in [1, 2, 3, 4, 5]:
                    print(inp)
                    self.game.clear_terminal()
                    return inp
                else:
                    print("Enter a valid choice!")
            except ValueError:
                print("Enter a valid choice!")

    def print_board(self, board):
        print("  1 2 3")
        for i, row in enumerate(board):
            print(f"{i + 1} {' '.join(row)}")
        print("\n")
