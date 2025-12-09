from sudoku_game import SudokuGame

sample_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def imperative_solver(sudoku: SudokuGame):
    empty_cells = []
    for r in range(9):
        for c in range(9):
            if sudoku.board[r][c] == 0:
                empty_cells.append((r, c))

    i = 0
    while 0 <= i < len(empty_cells):
        row, col = empty_cells[i]

        found_valid = False
        current_val = sudoku.board[row][col]

        for guess in range(current_val + 1, 10):
            if sudoku.is_valid(row, col, guess):
                sudoku.board[row][col] = guess
                found_valid = True
                i += 1  
                break

        if not found_valid:
            sudoku.board[row][col] = 0
            i -= 1

    return i == len(empty_cells)


if __name__ == "__main__":
    sudoku = SudokuGame(sample_board)
    sudoku.print_board()

    print("\n\n")

    imperative_solver(sudoku)
    sudoku.print_board()
