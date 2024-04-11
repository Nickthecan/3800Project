import socket, json

def start_game(clientsocket, board):
    current_player = 'X'

    print_board(board)
    player_move(current_player, board, clientsocket)

    winner_found, winning_symbol = check_winner(board)

    if winner_found:
        print_board(board)
        declare_winner(winning_symbol)
    elif check_if_full(board):
        print_board(board)
        print("It is a tie")
    else:
        #remove this later
        data = json.dumps({"board": board})
        clientsocket.send(data.encode())
        #remove the board

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

def player_move(current_player, board, clientsocket):
    row = int(input("Please select Row: "))
    column = int(input("Please select Column: "))

    if is_valid(row, column, board):
        board[row][column] = current_player
    else:
        print("Invalid Answer. Try Again")
        player_move(current_player, board)

def socket_connect_client():
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("socket created successfully")
    except socket.error as error:
        print("socket creation failed, {}".format(error))

    clientsocket.connect((socket.gethostname(), 8080))

    message = clientsocket.recv(1024)
    print(message.decode("utf-8"))

    board = [['', '', ''],['', '', ''],['', '', '']]

    while True:
        #need to turn this into a function that returns an array and then pass it through
        start_game(clientsocket, board)
        #message = input("Enter Row Number and Column Number: ")

        message_from_server = clientsocket.recv(1024)
        if message_from_server.decode() == "close":
            break



        clientsocket.sendall(message.encode())
    
    clientsocket.close()

socket_connect_client()
""" start_game() """