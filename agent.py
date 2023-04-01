
# Define the player colors
from utils import make_move, BLACK, WHITE, get_opponent


def terminal_test(board, player):

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

            elif board[i][j] == WHITE:
                if board[i+1][j] == WHITE:
                    number_w_adj += 1
                if board[i-1][j] == WHITE:
                    number_w_adj += 1
                if board[i][j+1] == WHITE:
                    number_w_adj += 1
                if board[i][j-1] == WHITE:
                    number_w_adj += 1
    return number_b_adj, number_w_adj


def second_evaluation_function(state):
    board = state[0]
    weights = [[3, 2, 2, 3],
               [2, 1, 1, 2],
               [2, 1, 1, 2],
               [3, 2, 2, 3]]

    player1_score = 0
    player2_score = 0

    for i in range(4):
        for j in range(4):
            if board[i][j] == BLACK:
                player1_score += weights[i][j]
            elif board[i][j] == WHITE:
                player2_score += weights[i][j]

    adj1, adj2 = find_adjacencies(board)
    value = (player1_score-adj1) - (player2_score-adj2)
    return value


def first_evaluation_function(state):
    board = state[0]
    weights = [[3, 2, 2, 3],
               [2, 1, 1, 2],
               [2, 1, 1, 2],
               [3, 2, 2, 3]]

    player1_score = 0
    player2_score = 0

    for i in range(4):
        for j in range(4):
            if board[i][j] == BLACK:
                player1_score += weights[i][j]
            elif board[i][j] == WHITE:
                player2_score += weights[i][j]
    value = player1_score - player2_score
    return value


def AlphaBetaPrunningDepth(state, depth, alpha, beta, maximizing_player, available_moves):
    board = state[0]
    player = state[1]

    if depth == 0 or (terminal_test(state[0], BLACK) > 0) or (terminal_test(state[0], WHITE) > 0):
        # return first_evaluation_function(state), 0
        return second_evaluation_function(state), 0

    if maximizing_player:
        max_value = float('-inf')
        best_move = None
        for move in available_moves:
            new_board = make_move(board, move, player)
            new_state = [new_board, get_opponent(player)]
            value, _ = AlphaBetaPrunningDepth(new_state, depth-1, alpha,
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
            new_board = make_move(board, move, player)
            new_state = [new_board, get_opponent(player)]
            value, _ = AlphaBetaPrunningDepth(new_state, depth-1, alpha,
                                              beta, True, available_moves)
            if value < min_value:
                min_value = value
                best_move = move
            beta = min(beta, min_value)
            if beta <= alpha:
                break
        return min_value, best_move
