import time
import random

# Define the heuristic function


def heuristic(state):
    # TODO: Implement your heuristic function here
    return 0

# Define the function for getting the available moves for a player


def get_available_moves(board, player):
    # TODO: Implement the function for getting available moves
    return []

# Define the function for making a move on the board


def make_move(board, move, player):
    # TODO: Implement the function for making a move
    return board

# Define the function for checking if a player has won


def check_win(board, player):
    # TODO: Implement the function for checking if a player has won
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
            move_str = input('Enter your move (e.g., C2 DR): ')
            move_from, move_dir = move_str.split()
            col = ord(move_from[0]) - ord('A')
            row = int(move_from[1]) - 1
            move = (row, col, move_dir)
            return move
        except ValueError:
            print('Invalid move. Please try again.')

# Define the function for getting the computer's move


""" 
def get_computer_move(state):
    global start_time
    start_time = time.time()
    #move = alpha_beta_search(state, MAX_DEPTH)
    return move
"""


def get_computer_move(state):
    # Define the available columns and rows
    columns = ['A', 'B', 'C', 'D']
    rows = [1, 2, 3, 4]
    # Choose a random column, row and direction
    column = random.choice(columns)
    row = random.choice(rows)
    direction = random.choice(['NW', 'NE', 'SW', 'SE'])
    # Return the random move
    return f"{column}{row} {direction}"


# Define the function for playing the game


def play_game(board):

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

            move = get_computer_move(state)
            board = make_move(board, move, player)
            display_board(board)
            if check_win(board, player):
                print('Sorry, you lose!')
                return
        # Switch the player
        player = WHITE if player == BLACK else BLACK


# Define the game board as a 4x4 matrix of None values
board = [[None for _ in range(4)] for _ in range(4)]
# Define the player colors
BLACK = 'B'
WHITE = 'W'

# Define the current player
player = BLACK

# Define the game state
state = (board, player)

# Define the maximum search depth for Minimax
MAX_DEPTH = 3

# Define the start time for measuring the computer's response time
start_time = None
play_game(board)
