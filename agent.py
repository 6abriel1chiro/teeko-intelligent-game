from game import *


"""
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'B' or 'W'.
"""


"""

class State:
    def __init__(self):
        self.father = None
        self.value = None
        self.utility = 0
        self.moves = moves
        self.player = player


def actions(self, state):
   # Legal moves are any square not yet taken.
    return state.moves


def result(self, state, move):
    if move not in state.moves:
        return state  # Illegal move has no effect
    board = board.copy()
    board[move] = state.to_move
    moves = list(state.moves)
    moves.remove(move)
    return nextMove


def utility(self, state, player):
   # Return the value to player; 1 for win, -1 for loss, 0 otherwise.
    return state.utility if player == 'B' else -state.utility


def terminal_test(self, state):
    #A state is terminal if it is won or there are no empty squares.
    return state.utility != 0 or len(state.moves) == 0


def compute_utility(self, board, move, player):
    # If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0.
    return 0


def eval_fn():
    boardWeights = [
        [0, 1, 0, 1, 0],
        [1, 2, 2, 2, 1],
        [0, 2, 3, 2, 0],
        [1, 2, 2, 2, 1],
        [0, 1, 0, 1, 0]
    ]
    for x in range(5):
        for y in range(5):
            if state.board[x][y] != 0:
                value = value + state.board[x][y] * boardWeights[x][y]

    return value


def alphabeta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    # The default test cuts off at depth d or at a terminal state
    best_score = -infinity
    beta = infinity
    best_action = None
    for a in game.actions(state):
        v = min_value(game.result(state, a), best_score, beta, 1)
        if v > best_score:
            best_score = v
            best_action = a
    return best_action

    # Functions used by alphabeta

    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = -infinity
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = infinity
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a),
                                 alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v




 """

"""  
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

    def evaluation_function(state):
        # Implement your own evaluation function here
        return 0

    def minimax(state, depth, alpha, beta, maximizing_player):
        if depth == 0 or check_win(state[0], BLACK) or check_win(state[0], WHITE):
            return evaluation_function(state), None

        if maximizing_player:
            max_value = float('-inf')
            best_move = None
            for move in available_moves:
                new_state = make_move(state[0], move, player)
                value, _ = minimax(new_state, depth-1, alpha, beta, False)
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
                value, _ = minimax(new_state, depth-1, alpha, beta, True)
                if value < min_value:
                    min_value = value
                    best_move = move
                beta = min(beta, min_value)
                if beta <= alpha:
                    break
            return min_value, best_move

    _, best_move = minimax(state, max_depth, float('-inf'), float('inf'), True)
    return best_move
"""
