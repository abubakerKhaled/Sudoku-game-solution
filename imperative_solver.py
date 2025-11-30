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
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def imperative_solver(sudoku: SudokuGame):
    row, col = sudoku.find_next_empty()

    if row is None:
        return True


    for guess in range(1, 10):
        if sudoku.is_valid(row, col, guess):
            sudoku.board[row][col] = guess

            if imperative_solver(sudoku):
                return True

            sudoku.board[row][col] = 0

    return False

if __name__ == "__main__":
    sudoku = SudokuGame(sample_board)
    sudoku.print_board()

    print("\n\n")

    imperative_solver(sudoku)
    sudoku.print_board()

