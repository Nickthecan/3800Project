#imports
import socket, json

#method to bind the server side to the client side. This starts the game
def socket_bind_server_play_game():
    #try block to create a server socket
    try:
        #create a socket binding specifying the type of socket to be created and the address family
        #AF_INET = communicate over IPv4 networks
        #SOCK_STREAM = type of socket to be created, creates a two-way connction-based type stream
        #              makes sure that data is delivered in order without any errors or duplications
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("socket created successfully")
    except socket.error as error:
        print("socket creation failed, {}".format(error))

    #binds the socket with the hostname of the local machine and the port number (random port number)
    serversocket.bind((socket.gethostname(), 8080))
    #listens for any client response
    serversocket.listen(5)
    #Once a client has been found, accept the client and connect the two together
    clientsocket, address = serversocket.accept()
    print("connection from {} has been established".format(address))
    clientsocket.send(bytes("Welcome to the Server", "utf-8"))

    #initalize the starting position of the board
    board = [['', '', ''],['', '', ''],['', '', '']]
    #server plays as O (player 2)
    current_player = 'O'
    print_board(board)
    print("Waiting for Client's Move...")

    #while the connection is secured, run a while loop to play the game
    while True:
        #since the server goes second, we listen for the client's message first
        data_from_client = clientsocket.recv(1024)
        #load board from json module
        data = json.loads(data_from_client.decode())
        #store into a 2D array variable
        board = data.get("board")

        #check to see if the server won in order to display it to the client, otherwise continue with the game
        winner_found = check_winner(board)
        if winner_found:
            print_board(board)
            print("You lost! Player X won")
            break
        elif check_if_full(board):
            print_board(board)
            print("It is a tie")
            break

        #print the board
        print_board(board)
        #make the server make a choice on where to play
        player_move(current_player, board) 
        #check for a winner after the server makes a move
        winner_found = check_winner(board)

        #conditional statement to see what to return
        #if server wins, declare server as winner and return a "close" statement to tell the socket to close
        if winner_found:
            print_board(board)
            declare_winner(current_player)
            client_data = json.dumps({"board": board})
            clientsocket.send(client_data.encode())
            break
        #if the board is full, declare a tie and return a "close" statement to tell the socket to close
        elif check_if_full(board):
            print_board(board)
            print("It is a tie")
            client_data = json.dumps({"board": board})
            clientsocket.send(client_data.encode())
            break
        #otherwise print the board and send to the client
        else:
            print_board(board)
            print("Waiting for Client's Move...")
            #send the updated response back to the client
            server_data = json.dumps({"board": board})
            clientsocket.send(server_data.encode())

    #Once the while loop breaks, close the connection for the server and client
    clientsocket.close()
    serversocket.close()
#end socket_bind_server

#method to print the board to the server
def print_board(board):
    print("  {}  |  {}  |  {}  ".format(board[0][0], board[0][1], board[0][2]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(board[1][0], board[1][1], board[1][2]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(board[2][0], board[2][1], board[2][2]))
#end print_board

#method for the server to play a move on the board
def player_move(current_player, board):
    #select row and column
    row = int(input("Please select Row: "))
    column = int(input("Please select Column: "))

    #conditional statement to check to see if the move chosen by the server is valid
    if is_valid(row, column, board):
        board[row][column] = current_player
    #repeat the method again until the server chooses a valid move
    else:
        print("Invalid Answer. Try Again")
        player_move(current_player, board)
#end player_move

#helper method for the player_move function to check if the move played by the server is a valid move 
def is_valid(row, column, board):
    if (row < 0 or row > 2) or (column < 0 or column > 2):
        return False
    
    if board[row][column] == '':
        return True
    return False
#end is_valid

#method to check if the board is full
def check_if_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return False
    return True
#end check_if_full

#method to check for a winner after a move has been played
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return True
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != '':
        return True
    if (board[2][0] == board[1][1] == board[0][2]) and board[2][0] != '':
        return True
    return False
#end check_winner

#method to declare the winner
def declare_winner(current_player):
    print("{} wins the game".format(current_player))
#end declare_winner

#start socket_bind_server
socket_bind_server_play_game()