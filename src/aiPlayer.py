from connect4 import *
from gameUI import *
import copy
AI = 2
HUMAN = 1
EMPTY = 0


def ai_move(board, gameUI):
    pygame.display.flip()
#    col = random.randint(0, board.COLS - 1)
#    col = choose_move(board, 2)
    col, minimax_score = minimax(board, 4, -math.inf, math.inf, True)
    pygame.time.wait(500)
    gameUI.displayCoin2(col)
    if board.check_win2():
        board.gameOver()
        pygame.display.flip()
        pygame.time.wait(1500)
        gameUI.displayWinner(int(board.check_win()))


def sum_chunk(chunk, token):
    opp_token = HUMAN
    if token == HUMAN:
        opp_token = AI
    h = 0
    if chunk.count(token) == 4:
        h += 100
    elif chunk.count(token) == 3 and chunk.count(EMPTY) == 1:
        h += 5
    elif chunk.count(token) == 2 and chunk.count(EMPTY) == 2:
        h += 2

    if chunk.count(opp_token) == 3 and chunk.count(EMPTY) == 1:
        h -= 4

    return h


def heuristic(board, token):
    h = 0

    # Center heuristic (better moves at the center)
    center_col = [i for i in list(board.board[:, board.COLS//2])]
    center_count = center_col.count(token)
    h += center_count * 3

    # Horizontal heuristic
    for row in range(board.ROWS):
        token_row = [i for i in list(board.board[row, :])]
        for col in range(board.COLS-3):
            chunk = token_row[col:col+4]
            h += sum_chunk(chunk, token)

    # Vertical heuristic
    for col in range(board.COLS):
        token_col = [i for i in list(board.board[:, col])]
        for row in range(board.ROWS-3):
            chunk = token_col[row:row+4]
            h += sum_chunk(chunk, token)

    # Diagonal bottom to up heuristic
    for row in range(board.ROWS-3):
        for col in range(board.COLS-3):
            chunk = [board.board[row+i][col+i] for i in range(4)]
            h += sum_chunk(chunk, token)

    # Diagonal up to bottom heuristic
    for row in range(board.ROWS-3):
        for col in range(board.COLS-3):
            chunk = [board.board[row+3-i][col+i] for i in range(4)]
            h += sum_chunk(chunk, token)

    return h


def choose_move(board, token):
    valid_moves = board.getValidMoves()
    best_heuristic = 0
    best_col = random.choice(valid_moves)
    for col in valid_moves:
        temp_board = copy.deepcopy(board)
        temp_board.add_token2(col)
        h = heuristic(temp_board, token)
        if h > best_heuristic:
            best_heuristic = h
            best_col = col
    return best_col


def check_terminal_node(board):
    return board.check_win2() or len(board.getValidMoves()) == 0


def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_moves = board.getValidMoves()
    terminal = check_terminal_node(board)
    if depth == 0 or terminal:
        if terminal:
            if board.check_win() == AI:
                return (None, 100000000000000)
            elif board.check_win() == HUMAN:
                return (None, -10000000000000)
            else:  # Game over
                return (None, 0)
        else:  # Depth is zero
            return (None, heuristic(board, AI))

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_moves)
        for col in valid_moves:
            temp_board = copy.deepcopy(board)
            temp_board.add_token2(col)
            new_heur = minimax(temp_board, depth - 1, alpha, beta, False)[1]
            if new_heur > value:
                value = new_heur
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_moves)
        for col in valid_moves:
            temp_board = copy.deepcopy(board)
            temp_board.add_token2(col)
            new_heur = minimax(temp_board, depth - 1, alpha, beta, True)[1]
            if new_heur < value:
                value = new_heur
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
