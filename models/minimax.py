class MinimaxPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        best_score = -float('inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = self.symbol
                    score = self.minimax(board, 0, False)
                    board[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner(board)
        if winner is not None:
            return winner

        if self.is_full(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = self.symbol
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            opponent_symbol = 'O' if self.symbol == 'X' else 'X'
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = opponent_symbol
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = ' '
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board):
        for row in board:
            if row.count(row[0]) == 3 and row[0] != ' ':
                return 1 if row[0] == self.symbol else -1

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                return 1 if board[0][col] == self.symbol else -1

        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return 1 if board[0][0] == self.symbol else -1

        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return 1 if board[0][2] == self.symbol else -1

        return None

    def is_full(self, board):
        return all(cell != ' ' for row in board for cell in row)
