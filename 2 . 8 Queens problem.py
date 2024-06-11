def print_board(board):
    for row in board:
        print(' '.join('Q' if col else '.' for col in row))
    print()

def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens_util(board, col, n):
    # If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = True

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution then backtrack
            board[i][col] = False

    # If queen cannot be placed in any row in this column col then return False
    return False

def solve_n_queens(n):
    board = [[False for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return

    print_board(board)

# Get the size of the board from the user
n = int(input("Enter the size of the board: "))

# Solve the N-queens problem and print the solution
solve_n_queens(n)
