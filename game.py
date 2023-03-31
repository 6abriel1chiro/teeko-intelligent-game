import time
import random
import math
# Define the player colors
BLACK = 'B'
WHITE = 'W'


def create_board():
    return [['B', 'V', 'V', 'W'],
            ['V', 'B', 'W', 'V'],
            ['V', 'W', 'B', 'B'],
            ['W', 'V', 'V', 'V']]

# Define the function for making a move on the board

def traducir(move):
    rowt, col = int(move[0]), move[1]
    row = rowt - 1
    column = ord(col) - ord('A')
    return row, column
def make_move(board, move, player):
    col, row, direction = move[0], int(move[1]), move[3:]
    i = row - 1
    j = ord(col) - ord('A')
    if i < 0 or i > 3 or j < 0 or j > 3:
        raise ValueError(
            "Invalid move: position out of range ")
    new_board = [row[:] for row in board]
    new_board[i][j] = 'V'
    if direction == 'NW':
        new_board[i-1][j-1] = player
    elif direction == 'N':
        new_board[i-1][j] = player
    elif direction == 'NE':
        new_board[i-1][j+1] = player
    elif direction == 'W':
        new_board[i][j-1] = player
    elif direction == 'E':
        new_board[i][j+1] = player
    elif direction == 'SW':
        new_board[i+1][j-1] = player
    elif direction == 'S':
        new_board[i+1][j] = player
    elif direction == 'SE':
        new_board[i+1][j+1] = player
    return new_board


# Define the function for checking if a player has won
def check_win(board, player):
    # Check rows
    for i in range(4):
        if board[i] == [player, player, player, player]:
            return True

    # Check columns
    for j in range(4):
        if [board[i][j] for i in range(4)] == [player, player, player, player]:
            return True

    # Check corners
    if board[0][0] == player and board[0][3] == player and board[3][0] == player and board[3][3] == player:
        return True

    # Check square
    for i in range(3):
        for j in range(3):
            if board[i][j] == player and board[i][j+1] == player and board[i+1][j] == player and board[i+1][j+1] == player:
                return True

    return False


# Define the function for displaying the game board


def display_board(board):
    print('   A   B   C   D')
    print('1  {} | {} | {} | {}'.format(
        board[0][0] or ' ', board[0][1] or ' ', board[0][2] or ' ', board[0][3] or ' '))
    print('  ---|---|---|---')
    print('2  {} | {} | {} | {}'.format(
        board[1][0] or ' ', board[1][1] or ' ', board[1][2] or ' ', board[1][3] or ' '))
    print('  ---|---|---|---')
    print('3  {} | {} | {} | {}'.format(
        board[2][0] or ' ', board[2][1] or ' ', board[2][2] or ' ', board[2][3] or ' '))
    print('  ---|---|---|---')
    print('4  {} | {} | {} | {}'.format(
        board[3][0] or ' ', board[3][1] or ' ', board[3][2] or ' ', board[3][3] or ' '))

# Define the function for getting user input for the move


def get_user_move():
    while True:
        try:
            move_str = input('Enter your move (e.g., C2 SE): ')
            return move_str
        except ValueError:
            print('Invalid move. Please try again.')

# Define the function for getting the computer's move


""" 
def get_computer_move(state):
    global start_time
    start_time = time.time()
    move = alpha_beta_search(state, MAX_DEPTH)
    return move

"""


def get_computer_move(state):
    # Define the available columns and rows
    columns = ['A', 'B', 'C', 'D']
    rows = [1, 2, 3, 4]
    # Choose a random column, row and direction
    column = random.choice(columns)
    row = random.choice(rows)
    direction = random.choice(['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE'])
    # Return the random move
    return f"{column}{row} {direction}"

def terminal_test(board, player):
    # Check rows
    for i in range(4):
        if board[i] == [player, player, player, player]:
            return True

    # Check columns
    for j in range(4):
        if [board[i][j] for i in range(4)] == [player, player, player, player]:
            return True

    # Check corners
    if board[0][0] == player and board[0][3] == player and board[3][0] == player and board[3][3] == player:
        return True

    # Check square
    for i in range(3):
        for j in range(3):
            if board[i][j] == player and board[i][j+1] == player and board[i+1][j] == player and board[i+1][j+1] == player:
                return True

    return False

def calculate_score(board,jugador):
    score = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == jugador:
                score += 1
    return score
def utility(board):
    player1_score = calculate_score(board, 1)
    player2_score = calculate_score(board, -1)
    return player1_score - player2_score

def is_possible_move(board, row, col, direction,color):
    # Verificar que la posición dada sea válida en el tablero
    if not (0 <= row < len(board) and 0 <= col < len(board[0])):
        return False

    # Verificar que la casilla en la que se encuentra la ficha a mover pertenezca al jugador actual
    if board[row][col] != color:
        
        return False

    # Verificar que la dirección sea válida
    if direction not in ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']:
        return False

    # Verificar que el movimiento no lleve a una posición fuera del tablero
    if (direction == 'N' and row == 0) or (direction == 'S' and row == len(board)-1) or \
       (direction == 'W' and col == 0) or (direction == 'E' and col == len(board[0])-1):
        return False
    if (direction == 'NW' and (row == 0 or col == 0)) or \
       (direction == 'NE' and (row == 0 or col == len(board[0])-1)) or \
       (direction == 'SW' and (row == len(board)-1 or col == 0)) or \
       (direction == 'SE' and (row == len(board)-1 or col == len(board[0])-1)):
        return False

    # Verificar que no haya otra ficha del mismo jugador en la casilla a la que se quiere mover
    if direction == 'N' and board[row-1][col] == color:
        return False
    if direction == 'S' and board[row+1][col] == color:
        return False
    if direction == 'W' and board[row][col-1] == color:
        return False
    if direction == 'E' and board[row][col+1] == color:
        return False
    if direction == 'NW' and board[row-1][col-1] == color:
        return False
    if direction == 'NE' and board[row-1][col+1] == color:
        return False
    if direction == 'SW' and board[row+1][col-1] == color:
        return False
    if direction == 'SE' and board[row+1][col+1] == color:
        return False

    return True

def possible_moves(board,color):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == color:
                for direction in ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']:
                    if is_possible_move(board, row, col, direction,color):
                        moves.append((row, col, direction))
    return moves

def result(board,move,color):
    i, j,direction= move[0],move[1],move[2]
    new_board = [row[:] for row in board]
    new_board[i][j] = 'V'
    if direction == 'N':
        new_board[i-1][j] = color
    elif direction == 'S':
        new_board[i+1][j] = color
    elif direction == 'E':
        new_board[i][j+1] = color
    elif direction == 'W':
        new_board[i][j-1] = color
    elif direction == 'NW':
        new_board[i-1][j-1] = color
    elif direction == 'NE':
        new_board[i-1][j+1] = color
    elif direction == 'SW':
        new_board[i+1][j-1] = color
    elif direction == 'SE':
        new_board[i+1][j+1] = color
    return new_board

def alpha_beta(board, depth, alpha, beta, maximizing_player,color):
    if depth == 0 or terminal_test(board,color):
        return None, utility(board)

    if maximizing_player:
        value = -math.inf
        best_move = None
        for move in possible_moves(board,color):
            result_board = result(board, move,color)
            _, temp_value = alpha_beta(result_board, depth-1, alpha, beta, False)
            if temp_value > value:
                value = temp_value
                best_move = move
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return best_move, value
    else:
        value = math.inf
        best_move = None
        for move in possible_moves(board,color):
            result_board = result(board, move,color)
            _, temp_value = alpha_beta(result_board, depth-1, alpha, beta, True)
            if temp_value < value:
                value = temp_value
                best_move = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_move, value

# Define the function for playing the game
def minmax(board, depth,color, utility, alpha, beta):
    if depth == 0 or terminal_test(board,color):
        return utility(board)

    if color:
        v = -math.inf
        for move in possible_moves(board,color):
            new_board = result(board, move,color)
            print(new_board)
            v = max(v, minmax(new_board, depth - 1, alpha, beta, False, utility))
            alpha = max(alpha, v)
            if beta <= alpha:
                break  # poda alpha-beta
        return v
    else:
        v = math.inf
        for move in possible_moves(board,color):
            new_board = result(board, move,color)
            print(new_board)
            v = min(v, minmax(new_board, depth - 1, alpha, beta, True, utility))
            beta = min(beta, v)
            if beta <= alpha:
                break  # poda alpha-beta
        return v
def play_game(state):

    board = state[0]

    # Display the game board
    display_board(board)

    # Let the user choose the color of the pieces
    human_player = None
    while human_player not in [BLACK, WHITE]:
        try:
            human_player = input(
                "Choose your color ('B' for Black, 'W' for White): ").upper()
        except ValueError:
            print('Invalid input. Please try again.')

    # Define the human player and the computer player
    if human_player == BLACK:
        computer_player = WHITE
    else:
        computer_player = BLACK

    player = random.choice([computer_player, human_player])
    print(player)
    # Loop until the game is over
    while True:
        # Let the human player make a move
        if player == human_player:
            print('HUMAN TURN')
            move = get_user_move()
            board = make_move(board, move, player)
            display_board(board)
            if check_win(board, player):
                print('Congratulations! You win!')
                return
        # Let the computer make a move
        else:
            print('AI TURN')

            # state will helps us expand possible states in the future, right now it is not being used
            move = get_computer_move(state)
            board = make_move(board, move, player)
            display_board(board)
            if check_win(board, player):
                print('Sorry, you lose!, AI wins')
                return
        # Switch the player
        player = WHITE if player == BLACK else BLACK

def play_game2(depth):
# Definir el tablero
    board = create_board()
    ai_color = ''
    # Definir el color del jugador humano
    player_color = input("¿Qué color desea usar? (B/W) ").upper()
    # Definir quién empieza a jugar
    current_player = 'human' if player_color == 'B' else 'ai'
    if player_color == 'B':
        ai_color = 'W'
    else:
        ai_color = 'B'
    # Mientras el juego no haya terminado
    while not terminal_test(board,current_player):
        display_board(board)

        if current_player == 'human':
        # Jugada del jugador humano
            mov = input("Ingrese la fila y columna de la ficha que desea mover: ")
            direction = input("Ingrese la dirección en la que desea mover la ficha (N, S, E, W, NW, NE, SW o SE): ")
            row,col = traducir(mov)
            move = [row,col,direction]
            if is_possible_move(board,row, col, direction, player_color):
                board = result(board, move, player_color)
                current_player = 'ai'
            else:
                print("Jugada no válida. Inténtalo de nuevo.")

        else:
        # Jugada de la IA
            alpha=-math.inf
            beta=math.inf
            #move = minmax(board,depth, ai_color,0,alpha,beta)
            #print(move)
            move = alpha_beta(board,depth,alpha,beta,ai_color)
            board = result(board, move[0], move[1], move[2], 'W' if player_color == 'B' else 'B')
            current_player = 'human'

# Imprimir el resultado final del juego
    display_board(board)
    print("¡Fin del juego! El ganador es " + utility(board, player_color))
curent_player = None


# Define the maximum search depth for Minimax
MAX_DEPTH = 3

# Define the start time for measuring the computer's response time
start_time = None


# Define the game board as a 4x4 matrix of None values
board = create_board()
# Define the game state
state = (board, curent_player)
play_game2(MAX_DEPTH)
