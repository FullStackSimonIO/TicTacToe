import json


class Game:
    def __init__(self):
        self.current_player = "X"

    def clear_terminal(self):
        # Methode, um das Terminal zu leeren
        print("\033[H\033[J", end="")

    def check_if_winner(self, board, symbol):
        # Überprüfung der Gewinnbedingungen
        # Reihen, Spalten und Diagonalen prüfen
        for row in board:
            if all([cell == symbol for cell in row]):
                return True

        for col in range(3):
            if all([board[row][col] == symbol for row in range(3)]):
                return True

        if all([board[i][i] == symbol for i in range(3)]) or all([board[i][2 - i] == symbol for i in range(3)]):
            return True

        return False

    def check_if_board_is_full(self, board):
        return all([cell != ' ' for row in board for cell in row])

    def switch_player(self):
        self.current__player = "O" if self.current_player == "X" else "X"

    def convert_to_json(self):
        return json.dumps({
            "current_player": self.current_player
        })

    def load_from_json(self, json_data):
        data = json.loads(json_data)
        self.current_player = data["current_player"]
