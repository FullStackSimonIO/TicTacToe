from models.board import Board
from models.game import Game
from models.player import HumanPlayer
from view.view import View


class PlayerVsPlayerPresenter:
    def __init__(self):
        self.board = Board()
        self.game = Game()
        self.view = View()
        self.player_1 = HumanPlayer(0, "Player 1", "X")
        self.player_2 = HumanPlayer(1, "Player 2", "O")

    def play_pvp_game(self):
        # Sicherstellen, dass das Spielfeld nur einmal zu Beginn zurückgesetzt wird
        self.board.reset_board()

        while True:
            # Zug von Spieler 1
            self.view.print_board(self.board.board)
            row, col = self.player_1.make_move(self.board.board)
            self.board.update_field(self.player_1.symbol, row, col)
            self.game.clear_terminal()
            self.view.print_board(self.board.board)

            if self.game.check_if_winner(self.board.board, self.player_1.symbol):
                print(f"{self.player_1.name} wins!")
                break

            if self.game.check_if_board_is_full(self.board.board):
                print("It's a draw!")
                break

            # Zug von Spieler 2
            row, col = self.player_2.make_move(self.board.board)
            self.board.update_field(self.player_2.symbol, row, col)
            self.game.clear_terminal()
            self.view.print_board(self.board.board)

            if self.game.check_if_winner(self.board.board, self.player_2.symbol):
                print(f"{self.player_2.name} wins!")
                break

            if self.game.check_if_board_is_full(self.board.board):
                print("It's a draw!")
                break
