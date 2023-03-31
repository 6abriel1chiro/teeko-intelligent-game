import time
import random
# from agent import *
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
    col = ord(move[0]) - ord('A')
    row = int(move[1]) - 1
    direction = move[3:]
    
    i, j = row, col
    previous_position = [i, j]
    if i < 0 or i > 3 or j < 0 or j > 3:
        raise ValueError(
            "Invalid move: position out of range ")
    new_board = [row[:] for row in board]
     #posible cambio
    if direction == 'NW':
        for n in range(1, min(i+1, j+1)+1):
            if new_board[i-n][j-n] is not None:
                break
            new_board[i-n][j-n] = player
            new_board[previous_position[0]][previous_position[1]] = None
            previous_position = [i-n, j-n]

    elif direction == 'N':
        for n in range(1, i+1):
            if new_board[i-n][j] is not None:
                break
            new_board[i-n][j] = player
            new_board[previous_position[0]][previous_position[1]] = None
            previous_position = [i-n, j]

    elif direction == 'NE':
        for n in range(1, min(i+1, 4-j)+1):
            if new_board[i-n][j+n] is not None:
                break
            new_board[i-n][j+n] = player
            new_board[previous_position[0]][previous_position[1]] = None
            previous_position = [i-n, j+n]

    elif direction == 'W':
        for n in range(1, j+1):
            if new_board[i][j-n] is not None:
                break
            new_board[i][j-n] = player
            new_board[previous_position[0]][previous_position[1]] = None
            previous_position = [i, j-n]

    elif direction == 'E':
        for n in range(1, 4-j):
            if new_board[i][j+n] is not None:
                break
            new_board[i][j+n] = player
            new_board[previous_position[0]][previous_position[1]] = None
            previous_position = [i, j+n]

    elif direction == 'SW':
        for n in range(1, min(4-i, j+1)+1):
            if new_board[i+n][j-n] is not None:
                break
            new_board[i+n][j-n] = player
            new_board[previous_position[0]][previous_position[1]] = None
            previous_position = [i+n, j-n]

    elif direction == 'S':
        for n in range(1, 4-i):
            if new_board[i+n][j] is not None:
                break
            new_board[i+n][j] = player
            new_board[previous_position[0]][previous_position[1]] = None
            previous_position = [i+n, j]

    elif direction == 'SE':
        for n in range(1, min(4-i, 4-j)+1):
            if new_board[i+n][j+n] is not None:
                break
            new_board[i+n][j+n] = player
            new_board[previous_position[0]][previous_position[1]] = None
            previous_position = [i+n, j+n]

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


def calculate_score(board, player):
    score = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player:
                score += 1
    return score


def evaluation_function(state):
    board = state[0]
    player = state[1]
    player1_score = calculate_score(board, player)
    player2_score = calculate_score(board, player)
    return player1_score - player2_score


def minimax(state, depth, alpha, beta, maximizing_player, available_moves):
    board = state[0]
    player = state[1]
    if depth == 0 or check_win(state[0], BLACK) or check_win(state[0], WHITE):
        return evaluation_function(state), None

    if maximizing_player:
        max_value = float('-inf')
        best_move = None
        for move in available_moves:
            new_state = make_move(state[0], move, player)
            value, _ = minimax(new_state, depth-1, alpha,
                               beta, False, available_moves)
            if value > max_value:
                max_value = value
                best_move = move
            alpha = max(alpha, max_value)
            if beta <= alpha:
                break
        return max_value, best_move

    else:
        min_value = float('inf')
        best_move = None
        for move in available_moves:
            new_state = make_move(state[0], move, get_opponent(player))
            value, _ = minimax(new_state, depth-1, alpha,
                               beta, True, available_moves)
            if value < min_value:
                min_value = value
                best_move = move
            beta = min(beta, min_value)
            if beta <= alpha:
                break
        return min_value, best_move


def get_computer_move(state):
    board = state[0]
    player = state[1]
    available_moves = []

    for i in range(4):
        for j in range(4):
            if board[i][j] == player:
                for direction in ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']:
                    move = f"{chr(ord('A') + j)}{i+1} {direction}"
                    available_moves.append(move)

    if not available_moves:
        return None

    max_depth = 3
    _, best_move = minimax(state, max_depth, float(
        '-inf'), float('inf'), True, available_moves)
    return best_move


def get_opponent(player):
    if player == BLACK:
        return WHITE
    else:
        return BLACK


# Define the function for playing the game

def play_game():
    board = create_board()
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

    # player = random.choice([computer_player, human_player])
    player = human_player
    state = (board, player)

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


play_game()
