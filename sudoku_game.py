class SudokuGame:
    def __init__(self, board):
        self.board = board
        self._board_valid()
        self.size = 9

    def _board_valid(self):
        if not self.board:
            raise ValueError("Board cannot be empty")

        if len(self.board) != 9 or any(len(row) != 9 for row in self.board):
            raise ValueError("Board must be 9x9")

        for row in self.board:
            for cell in row:
                if not isinstance(cell, int) or cell < 0 or cell > 9:
                    raise ValueError("Board cells must be integers between 0 and 9")

        if not self.is_board_valid():
            raise ValueError("Board is not valid")

    def is_board_valid(self):
        for row in range(9):
            for col in range(9):
                num = self.board[row][col]
                if num != 0 and not self.is_valid(row, col, num):
                    return False
        return True

    def is_valid(self, row, col, num):
        temp = self.board[row][col]
        self.board[row][col] = 0
        row_vals = self.board[row]
        if num in row_vals:
            return False

        col_vals = [self.board[i][col] for i in range(9)]
        if num in col_vals:
            return False

        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if self.board[r][c] == num:
                    return False

        self.board[row][col] = temp
        return True

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                print(self.board[i][j], end=" ")
            print()

    def find_next_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return (row, col)
        return None, None
