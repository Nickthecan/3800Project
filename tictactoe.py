board = [['', '', ''],['', '', ''],['', '', '']]

def start_game():
    while not(check_if_full()):
        print_board()
        player_move('X')
        if check_winner('X'):
            print_board()
            declare_winner('X')
            break
        print_board()
        player_move('O')
        if check_winner('O'):
            print_board()
            declare_winner('O')
            break

def print_board():
    print("  {}  |  {}  |  {}  ".format(board[0][0], board[0][1], board[0][2]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(board[1][0], board[1][1], board[1][2]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(board[2][0], board[2][1], board[2][2]))

def check_winner(choice):
    for i in range(3):
        if board[0][i] == choice and board[1][i] == choice and board[2][i] == choice:
            return True
    for i in range(3):
        if board[i][0] == choice and  board[i][1] == choice and board[i][2] == choice:
            return True
    if board[0][0] == choice and  board[1][1] == choice and board[2][2] == choice:
        return True
    if board[2][0] == choice and board[1][1] == choice and board[0][2] == choice:
        return True
    return False

def declare_winner(choice):
    print("{} wins the game".format(choice))
    return True;

def check_if_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return False
    print("It is a tie")
    return True

def player_move(choice):
    row = int(input("Please select Row: "))
    column = int(input("Please select Column: "))

    if is_valid(row, column):
        board[row][column] = choice
    else:
        print("Invalid Answer. Try Again")
        player_move(choice)

def is_valid(row, column):
    if (row < 0 or row > 2) or (column < 0 or column > 2):
        return False
    
    if board[row][column] == '':
        return True
    return False    

def main():
    start_game()

main()