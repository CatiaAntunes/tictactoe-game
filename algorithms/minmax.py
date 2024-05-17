from functions.game import *

def get_possible_moves(cells):
    moves = []
    for row in cells:
        for cell in row:
            if not cell.clicked:
                moves.append(cell)
    return moves

def minmax(cells, depth, maximizing_player):
    winner = check_winner()  # Adjusted to call check_winner without arguments
    if winner or depth == 0:
        return evaluate(winner)

    if maximizing_player:
        max_eval = float('-inf')
        for cell in get_possible_moves(cells):
            cell.click('O')  # Assuming 'O' is the symbol for the maximizing player
            eval = minmax(cells, depth - 1, False)
            cell.clicked = False  # Reset the clicked status
            cell.symbol = None  # Reset the symbol
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for cell in get_possible_moves(cells):
            cell.click('X')  # Assuming 'X' is the symbol for the minimizing player
            eval = minmax(cells, depth - 1, True)
            cell.clicked = False  # Reset the clicked status
            cell.symbol = None  # Reset the symbol
            min_eval = min(min_eval, eval)
        return min_eval

def evaluate(winner):
    if winner == 'O':
        return 10
    elif winner == 'X':
        return -10
    else:
        return 0
