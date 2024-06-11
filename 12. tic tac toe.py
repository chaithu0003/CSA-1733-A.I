# Python program for Tic Tac Toe game
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    for _ in range(9):
        print_board(board)
        row, col = map(int, input(f"Player {players[turn % 2]} enter row and column (0, 1, 2): ").split())
        if board[row][col] == ' ':
            board[row][col] = players[turn % 2]
            if check_winner(board, players[turn % 2]):
                print_board(board)
                print(f"Player {players[turn % 2]} wins!")
                return
            turn += 1
        else:
            print("Cell already taken. Try again.")
    print("It's a draw!")
    print_board(board)

# Sample output
tic_tac_toe()
