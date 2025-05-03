import math

# Initialize a 3x3 Tic-Tac-Toe board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


max_depth = 3  # Initial max depth

def print_board(board):
    """prints current state of board """
    string = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            string += str(board[i][j]) + " " 
        string += "\n"
    return string



def is_winner(board, player):
    """checks the given player has won or not ., return true , false """
    if (board[0][0] == board[0][1] == board[0][2] == player) or (board[1][0] == board[1][1] == board[1][2] == player) or (board[2][0] == board[2][1] == board[2][2] == player):#Row checks
        return True
    elif (board[0][0] == board[1][0] == board[2][0] == player) or (board[0][1] == board[1][1] == board[2][1] == player) or (board[0][2] == board[1][2] == board[2][2] == player):#Column checks
        return True
    elif (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    else:
        return False
    

def is_full(board):
    """returns True if the board is full else false"""
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' ':
                return False
    return True

def find_space(board):
    """returns the all empty spaces in the board """
    empty_spaces = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                empty_spaces.append((i,j))
    return empty_spaces

def heuristic(board):
    """Heuristic: open winning lines for X minus open winning lines for O"""
    lines = [
        # Rows
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Columns
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # Diagonals
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    x_score = 0
    o_score = 0

    for line in lines:
        x_count = 0
        o_count = 0
        for (i, j) in line:
            if board[i][j] == 'X':
                x_count += 1
            elif board[i][j] == 'O':
                o_count += 1
        if o_count == 0 and x_count > 0:
            x_score += 1
        elif x_count == 0 and o_count > 0:
            o_score += 1

    return x_score - o_score


def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'X'):
        return 10 - depth
    elif is_winner(board, 'O'):
        return depth - 10
    elif is_full(board):
        return 0
    elif depth >= max_depth:
        return heuristic(board)

    if is_maximizing:
        best_score = -math.inf
        for row, col in find_space(board):
            board[row][col] = 'X'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[row][col] = ' '
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for row, col in find_space(board):
            board[row][col] = 'O'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[row][col] = ' '
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def best_move():
    global max_depth
    move = None
    best_score = -math.inf
    for row, col in find_space(board):
        board[row][col] = 'X'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[row][col] = ' '
        if score > best_score:
            best_score = score
            move = (row, col)
    if move is None:
        max_depth += 1  # Increase depth if needed
        return best_move()
    return move

def main():
    print("TIC TAC TOE\n0 1 2\n3 4 5\n6 7 8")
    while True:
        num = int(input("Enter position number (0-8): "))
        if num < 0 or num > 8:
            print("Invalid move, try again.")
            continue
        row, col = divmod(num, 3)
        if board[row][col] != ' ':
            print("Invalid move, try again.")
            continue
        board[row][col] = 'O'

        if is_winner(board, 'O'):
            print(print_board(board))
            print("Congratulations, You win!")
            break
        if is_full(board):
            print(print_board(board))
            print("It's a draw.")
            break

        move = best_move()
        if move:
            row, col = move
            board[row][col] = 'X'
            print(print_board(board))
            print("\nAI played")
        if is_winner(board, 'X'):
            print(print_board(board))
            print("AI wins!")
            break
        if is_full(board):
            print(print_board(board))
            print("It's a draw.")
            break

main()
