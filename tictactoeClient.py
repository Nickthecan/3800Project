import socket

def close_sockets(clientsocket, serversocket):
    if clientsocket:
        clientsocket.close()
    serversocket.close()

def start_game():
    board = [['', '', ''],['', '', ''],['', '', '']]
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.connect((socket.gethostname(), 8080))

    while True:
        print_board(board)
        current_player = 'X'
        player_move(current_player, board)

        winner_found, winning_symbol = check_winner(board)
        if winner_found:
            print_board(board)
            declare_winner(winning_symbol)
            break
        elif check_if_full(board):
            print_board(board)
            print("It is a tie")
            break
        else:
            print_board(board)
            current_player = 'O'
            player_move(current_player, board)

    close_sockets(None, serversocket)

def print_board(board):
    print("  {}  |  {}  |  {}  ".format(board[0][0], board[0][1], board[0][2]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(board[1][0], board[1][1], board[1][2]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(board[2][0], board[2][1], board[2][2]))

def is_valid(row, column, board):
    if (row < 0 or row > 2) or (column < 0 or column > 2):
        return False
    
    if board[row][column] == '':
        return True
    return False

def check_if_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return False
    return True

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return True, board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return True, board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != '':
        return True, board[0][0]
    if (board[2][0] == board[1][1] == board[0][2]) and board[2][0] != '':
        return True, board[2][0]
    return False, None

def declare_winner(current_player):
    print("{} wins the game".format(current_player))

def player_move(current_player, board):
    row = int(input("Please select Row: "))
    column = int(input("Please select Column: "))

    if is_valid(row, column, board):
        board[row][column] = current_player
    else:
        print("Invalid Answer. Try Again")
        player_move(current_player, board)

if __name__ == "__main__":
    start_game()