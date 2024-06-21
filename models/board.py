import json


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def update_field(self, symbol, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = symbol

    def convert_board_to_json(self):
        return json.dumps(self.board)

    def load_from_json(self, json_board):
        self.board = json.loads(json_board)
