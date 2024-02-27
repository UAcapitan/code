"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board_):
    """
    Returns player who has the next turn on a board.
    """
    line_board = [j for i in board_ for j in i]
    
    if line_board.count(X) == line_board.count(O):
        return X
    else:
        return O


def actions(board_):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_list = []

    for n1, row in enumerate(board_):
        for n2, obj in enumerate(row):
            if obj == EMPTY:
                actions_list.append([n1,n2])
    
    return actions_list


def result(board_, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_ = copy.deepcopy(board_)

    i, j = action
    board_[i][j] = player(board_)

    return board_


def winner(board_):
    """
    Returns the winner of the game, if there is one.
    """
    board_lines = [
        board_[0],
        board_[1],
        board_[2],
        [board_[0][0], board_[1][0], board_[2][0]],
        [board_[0][1], board_[1][1], board_[2][1]],
        [board_[0][2], board_[1][2], board_[2][2]],
        [board_[0][0], board_[1][1], board_[2][2]],
        [board_[0][2], board_[1][1], board_[2][0]]
    ]

    for board_line in board_lines:
        if all(i == board_line[0] for i in board_line):
            return board_line[0]


def terminal(board_):
    """
    Returns True if game is over, False otherwise.
    """
    line_board = [j for i in board_ for j in i]

    if winner(board_) or not EMPTY in line_board:
        return True
    else:
        return False


def utility(board_):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    match winner(board_):
        case "X":
            return 1
        case "O":
            return -1
        case _:
            return 0


def min_value(board_):
    board_ = copy.deepcopy(board_)
    if terminal(board_):
        return utility(board_)
    v = math.inf
    for act in actions(board_):
        v = min(v, max_value(result(board_,act)))
    return v

def max_value(board_):
    board_ = copy.deepcopy(board_)
    if terminal(board_):
        return utility(board_)
    v = -math.inf
    for act in actions(board_):
        v = max(v, min_value(result(board_, act)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    results = []

    if player(board) == "X":
        board_copied = copy.deepcopy(board)
        for act in actions(board):
            result_ = [min_value(result(copy.deepcopy(board_copied),act)), act]
            results.append(result_)
        act = sorted(results, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == "O":
        board_copied = copy.deepcopy(board)
        for act in actions(board):
            result_ = [max_value(result(copy.deepcopy(board_copied),act)), act]
            results.append(result_)
        act = sorted(results, key=lambda x: x[0])[0][1]

    return act
