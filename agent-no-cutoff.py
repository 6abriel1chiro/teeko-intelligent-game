import time
import random
import sys
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


def directions_to_move(direction, new_board, row_copy, col_copy, previous_position, player):
    if direction == 'NW':
        for n in range(1, min(row_copy+1, col_copy+1)+1):
            if row_copy-n >= 0 and col_copy >= 0:
                if new_board[row_copy-n][col_copy-n] is not None:
                    break
                new_board[row_copy-n][col_copy-n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy-n, col_copy-n]

    elif direction == 'N':
        for n in range(1, row_copy+1):
            if row_copy-n >= 0:
                if new_board[row_copy-n][col_copy] is not None:
                    break
                new_board[row_copy-n][col_copy] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy-n, col_copy]

    elif direction == 'NE':
        for n in range(1, min(row_copy+1, 4-col_copy)+1):
            if row_copy-n >= 0 and col_copy+n < 4:
                if new_board[row_copy-n][col_copy+n] is not None:
                    break
                new_board[row_copy-n][col_copy+n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy-n, col_copy+n]

    elif direction == 'W':
        for n in range(1, col_copy+1):
            if col_copy-n >= 0:
                if new_board[row_copy][col_copy-n] is not None:
                    break
                new_board[row_copy][col_copy-n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy, col_copy-n]

    elif direction == 'E':
        for n in range(1, 4-col_copy):
            if col_copy+n < 4:
                if new_board[row_copy][col_copy+n] is not None:
                    break
                new_board[row_copy][col_copy+n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy, col_copy+n]

    elif direction == 'SW':
        for n in range(1, min(4-row_copy, col_copy+1)+1):
            if row_copy+n < 4 and col_copy-n > 0:
                if new_board[row_copy+n][col_copy-n] is not None:
                    break
                new_board[row_copy+n][col_copy-n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy+n, col_copy-n]

    elif direction == 'S':
        for n in range(1, 4-row_copy):
            if row_copy+n < 4:
                if new_board[row_copy+n][col_copy] is not None:
                    break
                new_board[row_copy+n][col_copy] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy+n, col_copy]

    elif direction == 'SE':
        for n in range(1, min(4-row_copy, 4-col_copy)+1):
            if row_copy+n < 4 and col_copy+n < 4:
                if new_board[row_copy+n][col_copy+n] is not None:
                    break
                new_board[row_copy+n][col_copy+n] = player
                new_board[previous_position[0]][previous_position[1]] = None
                previous_position = [row_copy+n, col_copy+n]
    return new_board


def make_move(board, move, player):
    col = ord(move[0]) - ord('A')
    row = int(move[1]) - 1
    direction = move[3:]

    row_copy, col_copy = row, col
    previous_position = [row_copy, col_copy]

    if row_copy < 0 or row_copy > 3 or col_copy < 0 or col_copy > 3:
        raise ValueError(
            "Invalid move: position out of range ")

    new_board = [row[:] for row in board]

    return directions_to_move(direction, new_board, row_copy, col_copy, previous_position, player)


# Define the function for checking if a player has won
def check_win(board, player):

    for i in range(4):
        if board[i] == [player, player, player, player]:
            return True

    for j in range(4):
        if [board[x][j] for x in range(4)] == [player, player, player, player]:
            return True

    if board[0][0] == player and board[0][3] == player and board[3][0] == player and board[3][3] == player:
        return True

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
            return move_str.upper()
        except ValueError:
            print('Invalid move. Please try again.')


def find_adjacencies(board):
    number_b_adj = 0
    number_w_adj = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == BLACK:
                if board[i+1][j] == BLACK:
                    number_b_adj += 1
                if board[i-1][j] == BLACK:
                    number_b_adj += 1
                if board[i][j+1] == BLACK:
                    number_b_adj += 1
                if board[i][j-1] == BLACK:
                    number_b_adj += 1
                if board[i+1][j-1] == BLACK:
                    number_b_adj += 1
                if board[i+1][j+1] == BLACK:
                    number_b_adj += 1
                if board[i-1][j+1] == BLACK:
                    number_b_adj += 1
                if board[i-1][j-1] == BLACK:
                    number_b_adj += 1

            elif board[i][j] == WHITE:
                if board[i+1][j] == WHITE:
                    number_w_adj += 1
                if board[i-1][j] == WHITE:
                    number_w_adj += 1
                if board[i][j+1] == WHITE:
                    number_w_adj += 1
                if board[i][j-1] == WHITE:
                    number_w_adj += 1
                if board[i+1][j-1] == WHITE:
                    number_w_adj += 1
                if board[i+1][j+1] == WHITE:
                    number_w_adj += 1
                if board[i-1][j+1] == WHITE:
                    number_w_adj += 1
                if board[i-1][j-1] == WHITE:
                    number_w_adj += 1

    return number_b_adj, number_w_adj


def utility(state):
    opponent = get_opponent(state[1])
    if check_win(state[0], state[1]):
        return 100
    elif check_win(state[1], opponent):
        return -100
    else:
        return 0


def AlphaBetaPrunning(state, alpha, beta, maximizing_player, available_moves):
    board = state[0]
    player = state[1]

    if (check_win(state[0], BLACK)) or (check_win(state[0], WHITE)):
        return utility(state), 0

    if maximizing_player:
        max_value = float('-inf')
        best_move = None
        for move in available_moves:
            new_board = make_move(board, move, player)
            new_state = [new_board, get_opponent(player)]
            value, _ = AlphaBetaPrunning(new_state, alpha,
                                         beta, False, available_moves)
            if value > max_value:
                max_value = value
                best_move = move
            alpha = max(alpha, max_value)
            if beta <= alpha:
                print(board)

        return max_value, best_move

    else:
        min_value = float('inf')
        best_move = None
        for move in available_moves:
            new_board = make_move(board, move, player)
            new_state = [new_board, get_opponent(player)]
            value, _ = AlphaBetaPrunning(new_state, alpha,
                                         beta, True, available_moves)
            if value < min_value:
                min_value = value
                best_move = move
            beta = min(beta, min_value)
            if beta <= alpha:
                print(board)

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

    _, best_move = AlphaBetaPrunning(state, float(
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

    player = random.choice([computer_player, human_player])
    # player = human_player
    # player = computer_player
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


sys.setrecursionlimit(2000000)
play_game()
