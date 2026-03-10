import math

board = [
['_','_','_'],
['_','_','_'],
['_','_','_']
]

def print_board():
    for row in board:
        print(" ".join(row))
    print()

def is_moves_left():
    for i in range(3):
        for j in range(3):
            if board[i][j]=='_':
                return True
    return False

def evaluate():

    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2] and board[row][0] != '_':
            if board[row][0]=='X':
                return 10
            else:
                return -10

    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col] != '_':
            if board[0][col]=='X':
                return 10
            else:
                return -10

    if board[0][0]==board[1][1]==board[2][2] and board[0][0] != '_':
        if board[0][0]=='X':
            return 10
        else:
            return -10

    if board[0][2]==board[1][1]==board[2][0] and board[0][2] != '_':
        if board[0][2]=='X':
            return 10
        else:
            return -10

    return 0


def minimax(depth, isMax):

    score = evaluate()

    if score == 10:
        return score

    if score == -10:
        return score

    if not is_moves_left():
        return 0

    if isMax:

        best = -math.inf

        for i in range(3):
            for j in range(3):

                if board[i][j]=='_':

                    board[i][j]='X'
                    best = max(best, minimax(depth+1, False))
                    board[i][j]='_'

        return best

    else:

        best = math.inf

        for i in range(3):
            for j in range(3):

                if board[i][j]=='_':

                    board[i][j]='O'
                    best = min(best, minimax(depth+1, True))
                    board[i][j]='_'

        return best


def find_best_move():

    best_val = -math.inf
    best_move = (-1,-1)

    for i in range(3):
        for j in range(3):

            if board[i][j]=='_':

                board[i][j]='X'

                move_val = minimax(0, False)

                board[i][j]='_'

                if move_val > best_val:
                    best_move = (i,j)
                    best_val = move_val

    return best_move


def get_user_input():

    while True:
        try:
            r = int(input("Enter row (0-2): "))
            c = int(input("Enter column (0-2): "))

            if r not in [0,1,2] or c not in [0,1,2]:
                print("Enter values between 0 and 2.")
                continue

            if board[r][c] != '_':
                print("Cell already occupied. Try another.")
                continue

            return r,c

        except ValueError:
            print("Invalid input! Please enter numbers only.")


def play():

    print("TIC TAC TOE")
    print("Human = O  Computer = X\n")

    while True:

        print_board()

        r,c = get_user_input()

        board[r][c] = 'O'

        if evaluate() == -10:
            print_board()
            print("Human Wins!")
            break

        if not is_moves_left():
            print("Draw")
            break

        print("Computer Move")

        move = find_best_move()

        board[move[0]][move[1]] = 'X'

        if evaluate() == 10:
            print_board()
            print("Computer Wins!")
            break

        if not is_moves_left():
            print_board()
            print("Draw")
            break


play()
