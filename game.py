import time
import random

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


# Define the function for playing the game


def play_game():
    board = create_board()
    state = (board, BLACK)
    display_board(board)

    human_player = None
    while human_player not in [BLACK, WHITE]:
        try:
            human_player = input(
                "Choose your color ('B' for Black, 'W' for White): ").upper()
        except ValueError:
            print('Invalid input. Please try again.')

    if human_player == BLACK:
        computer_player = WHITE
    else:
        computer_player = BLACK

    player = random.choice([computer_player, human_player])

    while not check_win(board, BLACK) and not check_win(board, WHITE):
        if player == human_player:
            move = get_user_move()
        else:
            move = get_computer_move(state)
            print("Computer's move: ", move)

        try:
            board = make_move(board, move, player)
            state = (board, get_opponent(player))
            display_board(board)
        except ValueError as e:
            print(e)

        player = get_opponent(player)

    print('Game over! Winner: ', get_opponent(player))
