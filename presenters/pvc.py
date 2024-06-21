from models.board import Board
from models.game import Game
from models.player import HumanPlayer
from models.minimax import MinimaxPlayer
from view.view import View


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
            self.game.clear_terminal()
            self.view.print_board(self.board.board)

            if self.game.check_if_winner(self.board.board, self.computer.symbol):
                print("Computer wins!")
                break

            if self.game.check_if_board_is_full(self.board.board):
                print("It's a draw!")
                break

    def save_game(self, filename):
        game_data = {
            "board": self.board.convert_board_to_json(),
            "current_player": self.game.convert_to_json(),
            "human_player": {
                "symbol": self.player.symbol,
            },
            "computer_player": {
                "symbol": self.computer.symbol,
            }
        }
        with open(filename, "w") as file:
            file.write(str(game_data))

    def load_game(self, filename):
        with open(filename, "r") as file:
            game_data = eval(file.read())
        self.board.load_from_json(game_data["board"])
        self.game.load_from_json(game_data["current_player"])
        self.player.symbol = game_data["human_player"]["symbol"]
        self.computer.symbol = game_data["computer_player"]["symbol"]
