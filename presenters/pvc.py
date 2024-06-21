from models.board import Board
from models.game import Game
from models.player import HumanPlayer, ComputerPlayer
from view.view import View


class PlayerVsComputerPresenter:

    def __init__(self):
        self.board = Board()
        self.game = Game()
        self.view = View()
        self.player = HumanPlayer(0, "Player", "X")
        self.computer = ComputerPlayer("Computer", "O")

    def play_pvc_game(self):
        # Player Turn
        self.view.print_board(self.board.board)
        row, col = self.player.make_move(self.board.board)
        self.board.update_field(self.player.symbol, row, col)
        self.game.clear_terminal()
        self.view.print_board(self.board.board)

        if self.game.chec_if_winner(self.board.board, self.player.symbol):
            print(f"{self.player.name} wins!")
            return

        if self.game.check_if_board_is_full(self.board.board):
            print("It's a draw!")
            return

        # Computer Turn
        row, col = self.computer.make_move(self.board.board)
        self.board.update_field(self.computer.symbol, row, col)
        self.game.clear_terminal()
        self.view.print_board(self.board.board)

        if self.game.check_if_winner(self.board.board, self.computer.symbol):
            print(f"{self.computer.name} wins!")
            return

        if self.game.check_if_board_is_full(self.board.board):
            print("It's a draw!")
            return
