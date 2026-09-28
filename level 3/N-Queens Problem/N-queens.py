'''

Description: Solve the classic N-Queens problem
where the goal is to place N queens on an N x N
chessboard such that no two queens threaten each
other.
Task 3: N-Queens Problem
Represent the chessboard as a 2D array.
Use backtracking to place queens one by one in safe
positions.
Ensure that no two queens are on the same row,
column, or diagonal.
Objectives:
Challenges: Designing an efficient backtracking solution
and correctly handling constraints

'''


def create_board(n):
    board = []
    for i in range(n):
        row = ['.'] * n
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_safe(board, row, col):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row):
    n = len(board)
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            if solve_n_queens_util(board, row + 1):
                return True
            board[row][col] = '.'

    return False
def solve_n_queens(n):
    board = create_board(n)
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return
    print_board(board)

def main():
    n = int(input("Enter the number of queens (N): "))
    solve_n_queens(n)

if __name__ == "__main__":
    main()



    