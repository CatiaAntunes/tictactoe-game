from functions.game import *

def get_possible_moves(cells):
    moves = []
    for row in cells:
        for cell in row:
            if not cell.clicked:
                moves.append(cell)
    return moves

def minmax(cells, depth, ai_turn):
    winner = check_winner()  # Adjusted to call check_winner without arguments
    if winner or depth == 0:
        return evaluate(winner)

    if ai_turn:
        max_eval = float('-inf')
        for cell in get_possible_moves(cells):
            cell.click('O')  # Assuming 'O' is the symbol for the maximizing player
            eval = minmax(cells, depth - 1, False) # Adjusted to call minmax with the correct arguments
            cell.clicked = False  # Reset the clicked status
            cell.symbol = None  # Reset the symbol
            max_eval = max(max_eval, eval) # Update the maximum evaluation
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
        return 1
    elif winner == 'X':
        return -1
    else:
        return 0
