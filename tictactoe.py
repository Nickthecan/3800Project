game_board = [['', '', ''], ['', '', ''], ['', '', '']]

def play_game():
    while not board_full():
        show_board()
        make_move('X')
        if check_win('X'):
            show_board()
            announce_winner('X')
            break
        show_board()
        make_move('O')
        if check_win('O'):
            show_board()
            announce_winner('O')
            break

def show_board():
    print("  {}  |  {}  |  {}  ".format(game_board[0][0], game_board[0][1], game_board[0][2]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(game_board[1][0], game_board[1][1], game_board[1][2]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(game_board[2][0], game_board[2][1], game_board[2][2]))

def check_win(symbol):
    for i in range(3):
        if game_board[0][i] == symbol and game_board[1][i] == symbol and game_board[2][i] == symbol:
            return True
    for i in range(3):
        if game_board[i][0] == symbol and  game_board[i][1] == symbol and game_board[i][2] == symbol:
            return True
    if game_board[0][0] == symbol and  game_board[1][1] == symbol and game_board[2][2] == symbol:
        return True
    if game_board[2][0] == symbol and game_board[1][1] == symbol and game_board[0][2] == symbol:
        return True
    return False

def announce_winner(symbol):
    print("{} emerges victorious!".format(symbol))
    return True

def board_full():
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == '':
                return False
    print("It's a tie!")
    return True

def make_move(symbol):
    row = int(input("Choose Row: "))
    column = int(input("Choose Column: "))

    if is_valid_move(row, column):
        game_board[row][column] = symbol
    else:
        print("Invalid move. Try again.")
        make_move(symbol)

def is_valid_move(row, column):
    if (row < 0 or row > 2) or (column < 0 or column > 2):
        return False

    if game_board[row][column] == '':
        return True
    return False    

def start():
    play_game()

start()