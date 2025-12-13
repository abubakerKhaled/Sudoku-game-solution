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


def create_new_row(old_row, col, value):
    return old_row[:col] + [value] + old_row[col + 1:]

def create_board_with_value(board: list[list], row: int, col: int, value: int):
    new_row = create_new_row(board[row], col, value)
    
    # Build new board: rows before + new row + rows after
    new_board = board[:row] + [new_row] + board[row + 1:]
    
    return new_board

def try_numbers(sudoku: SudokuGame, row: int, col: int, guess: int):
    if guess > 9:
        return None
    
    if sudoku.is_valid(row, col, guess):
        new_board = create_board_with_value(sudoku.board, row, col, guess)
        
        result = functional_solver(SudokuGame(new_board))
        
        if result is not None:
            return result
        
        return try_numbers(sudoku, row, col, guess + 1)
    else:
        return try_numbers(sudoku, row, col, guess + 1)


def functional_solver(sudoku: SudokuGame):
    row, col = sudoku.find_next_empty()

    if row is None or col is None:
        return sudoku

    return try_numbers(sudoku, row, col, 1)


if __name__ == "__main__":
    print("PURE FUNCTIONAL SUDOKU SOLVER")
    print("=" * 50)
    print("No loops - only recursion!")
    print("=" * 50)
    
    sudoku = SudokuGame(sample_board)
    print("\nORIGINAL PUZZLE:")
    sudoku.print_board()

    print("\n\nSOLVING...\n")

    result = functional_solver(sudoku)
    
    if result is not None:
        print("SOLUTION FOUND!")
        print("\nSOLVED PUZZLE:")
        result.print_board()
    else:
        print("No solution exists")