from models.board import Board
from models.game import Game
from models.player import HumanPlayer
from models.minimax import MinimaxPlayer
from view.view import View
from models.state import save_game


class PlayerVsComputerPresenter:

    def __init__(self):
        self.board = Board()
        self.game = Game()
        self.view = View()
        self.player = HumanPlayer(0, "Player", "X")
        self.computer = MinimaxPlayer("O")

    def play_pvc_game(self):
        self.board.reset_board()
        while True:

            # Player Turn
            self.view.print_board(self.board.board)
            row, col = self.player.enter_move(self.board.board)
            self.board.update_field(self.player.symbol, row, col)
            save_game("game.json", self.board, self.game,
                      self.player, self.computer)
            self.game.clear_terminal()
            self.view.print_board(self.board.board)

            if self.game.check_if_winner(self.board.board, self.player.symbol):
                print(f"{self.player.name} wins!")
                break

            if self.game.check_if_board_is_full(self.board.board):
                print("It's a draw!")
                break

            # Computer Turn
            row, col = self.computer.make_move(self.board.board)
            self.board.update_field(self.computer.symbol, row, col)
            save_game("state.json", self.board, self.game,
                      self.player, self.computer)
            self.game.clear_terminal()
            self.view.print_board(self.board.board)

            if self.game.check_if_winner(self.board.board, self.computer.symbol):
                print("Computer wins!")
                break

            if self.game.check_if_board_is_full(self.board.board):
                print("It's a draw!")
                break
