import math

# 棋盘：3x3，用 'X'（AI）和 'O'（人类）
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# 判断是否有赢家
def check_winner(board):
    # 行 / 列
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # 对角线
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# 是否结束
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# 评分函数
def evaluate(board):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    else:
        return 0

# Minimax 核心
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # 终止条件
    if score != 0:
        return score
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    value = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best = max(best, value)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    value = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best = min(best, value)
        return best

# 找最佳走法
def best_move(board):
    best_val = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)

    return move