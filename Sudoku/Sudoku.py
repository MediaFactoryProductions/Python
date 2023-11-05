import random 

def print_board(board):
    for i in range(9):

        if i % 3 == 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0:
                print("|", end= " ")
            print(board[i][j], end = " ")
        print()
#print(print_board)

def generate_sudoku():
    board = [['*' for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    shuffle_sudoku(board)
    return board

#sudoku_board = generate_sudoku()
#print_board(sudoku_board)

def is_valid(board, row, col, num):
    if num == '*':
        return True

    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    row_start, col_start = 3 * (row // 3), 3 * (col // 3)

    for i in range(3):
        for j in range(3):
            if board[row_start + i][col_start + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == '*':
                for num in map(str, range(1, 10)):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = '*'
                return False
    return True

def shuffle_sudoku(board):
    original_board = [row[:] for row in board]
    num_iterations = 100

    for _ in range(num_iterations):
        transformation = random.randint(1, 2)

        if transformation == 1:
            region = random.randint(0, 2)
            row1, row2 = random.sample(range(region * 3, (region + 1) * 3), 2)
            board[row1], board[row2] = board[row2], board[row1]
        
        elif transformation == 2:
            region = random.randint(0, 2)
            col1, col2 = random.sample(range(region * 3, (region + 1) * 3), 2)
            for i in range(9):
                board[i][col1], board[i][col2] = board[i][col2], board[i][col1]

        # After each transformation, check if the board is still valid
        if not solve_sudoku(board):
            # If it's not valid, revert to the original board
            for i in range(9):
                for j in range(9):
                    board[i][j] = original_board[i][j]

def make_user_puzzle(board, blank_values):
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)

    for i in range(blank_values):
        row, col = cells[i]
        board[row][col] = '*'

sudoku_board = generate_sudoku()
print("Solved Puzzle")
print_board(sudoku_board)

blank_values = 50
make_user_puzzle(sudoku_board, blank_values)
print("Unsolved Sudoku Puzzle")
print_board(sudoku_board)
