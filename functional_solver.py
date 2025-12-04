from sudoku_game import SudokuGame
import copy


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


def create_board_with_value(board: list[list], row: int, col: int, value: int):
    new_board = copy.deepcopy(board)
    new_board[row][col] = value
    return new_board

def functional_solver(sudoku: SudokuGame):
    row , col = sudoku.find_next_empty()

    if row is None or col is None:
        return sudoku

    for guess in range(1, 10):
        if sudoku.is_valid(row, col, guess):
            new_board = create_board_with_value(sudoku.board, row, col, guess)
            result = functional_solver(SudokuGame(new_board))
            if result:
                return result

    return None


if __name__ == "__main__":
    sudoku = SudokuGame(sample_board)
    sudoku.print_board()

    print("\n\n")

    result = functional_solver(sudoku)
    if result is not None:
        result.print_board()
    else:
        print("No solution exists")