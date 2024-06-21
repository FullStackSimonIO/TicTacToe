from models.game import Game


class Player:

    def __init__(self, index, name, symbol):
        self.index = index
        self.name = name
        self.symbol = symbol

    def enter_move(self, board):
        while True:
            try:
                cell = int(
                    input("Enter the Field (1-9) where you want to place your Icon...\n"))
                if cell < 1 or cell > 9:
                    print("Enter a Number between 1-9!")

                row, col = (cell - 1) // 3, (cell - 1) % 3
                if board[row][col] in ["X", "O"]:
                    print("Field already taken!")
                return row, col
            except ValueError:
                print("Enter a valid field!")


class HumanPlayer(Player):

    def __init__(self, index, name, symbol):
        super().__init__(index, name, symbol)

    def make_move(self, board):
        while True:
            try:
                cell = int(
                    input("Enter the Field (1-9) where you want to place your Icon...\n"))
                if cell < 1 or cell > 9:
                    print("Enter a Number between 1-9!")

                row, col = (cell - 1) // 3, (cell - 1) % 3
                if board[row][col] in ["X", "O"]:
                    print("Field already taken!")
                return row, col
            except ValueError:
                print("Enter a valid field!")


class ComputerPlayer:

    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        best_score = -1000
        best_move = None

        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = self.symbol
                    score = self.minimax(board, 0, False)
                    board[row][col] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner(board)
        if winner:
            return winner
        if self.is_full(board):
            return 0

        if is_maximizing:
            best_score = -1000
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = self.symbol
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            human_player = "0" if self.symbol == "X" else "X"
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = human_player
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = " "
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board):
        for row in board:
            if row.count(row[0]) == 3 and row[0] != " ":
                return 1 if row[0] == self.symbol else -1

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return 1 if board[0][col] == self.symbol else -1

        if board[0][0] == board[1][1] == board[2][2] != " ":
            return 1 if board[0][0] == self.symbol else -1

        if board[0][2] == board[1][1] == board[2][0] != " ":
            return 1 if board[0][2] == self.symbol else -1

        return 0

    def check_is_full(self, board):
        return all([cell != " " for row in board for cell in row])
