import time
import random
import math
# Define the player colors
BLACK = 'B'
WHITE = 'W'


def create_board():
    board = [[None for j in range(4)] for i in range(4)]
    board[0][0] = 'B'
    board[0][3] = 'W'
    board[1][1] = 'B'
    board[1][2] = 'W'
    board[2][1] = 'W'
    board[2][2] = 'B'
    board[3][0] = 'W'
    board[3][3] = 'B'
    return board

# Define the function for making a move on the board


def make_move(board, move, player):
    col, row, direction = move[0], int(move[1]), move[3:]
    i = row - 1
    j = ord(col) - ord('A')
    if i < 0 or i > 3 or j < 0 or j > 3:
        raise ValueError(
            "Invalid move: position out of range ")
    new_board = [row[:] for row in board]
    new_board[i][j] = None
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

def terminal_test(board):
    # Comprueba si hay una línea de cuatro fichas del mismo color (horizontal)
    for row in range(7):
        for col in range(4):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                return True
    
    # Comprueba si hay una línea de cuatro fichas del mismo color (vertical)
    for row in range(4):
        for col in range(7):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                return True
    
    # Comprueba si hay una ficha del mismo color en cada esquina 
    
            if board[0][0] == board[0][3] == board[3][0] == board[3][3] :
                return True
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

def is_legal_move(board, row, col, player):
    i = row - 1
    j = ord(col) - ord('A')
    if i < 0 or i > 3 or j < 0 or j > 3:
        return False
    return True
def possible_moves(board, player):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == None:
                # La celda está vacía, se puede realizar un movimiento
                if is_legal_move(board, row, col, player):
                    # El movimiento es legal, se agrega a la lista de movimientos
                    moves.append((row, col))
    return moves

def result(board, move, player):
    new_board = [row[:] for row in board]
    for row in range(6, -1, -1):
        if new_board[row][move] == None:
            new_board[row][move] = player
            break
    return new_board


# Define the function for playing the game
def minimax(board, depth, maximizing_player, alpha, beta):
    # Comprobar si se ha llegado al estado final o si se ha alcanzado el límite de profundidad
    if depth == 0 or terminal_test(board):
        return utility(board)
    
    # Si el jugador es 'Max', elegir el movimiento que maximiza el resultado de minimax
    if maximizing_player:
        best_action = None
        value = -math.inf
        for move in possible_moves(board):
            result_board = result(board, move, maximizing_player)
            _, new_value = minimax(result_board,depth-1,maximizing_player, alpha, beta)
            if new_value > value:
                value = new_value
                best_action = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_action, value
    
    # Si el jugador es 'Min', elegir el movimiento que minimiza el resultado de minimax
    else:
        best_value = float('inf')
        for move in possible_moves(board):
            result_board = result(board, move, maximizing_player)
            _, new_value = minimax(result_board,depth-1,maximizing_player, alpha, beta)
            if new_value < value:
                value = new_value
                best_action = move
            alpha = min(alpha, value)
            if alpha >= beta:
                break
        return best_action, value

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


curent_player = None


# Define the maximum search depth for Minimax
MAX_DEPTH = 3

# Define the start time for measuring the computer's response time
start_time = None


# Define the game board as a 4x4 matrix of None values
board = create_board()
# Define the game state
state = (board, curent_player)
play_game(state)
