from functions.game import *

def get_possible_moves(cells):
    # Function to return all possible moves (unclicked cells) on the board.
    moves = []
    for row in cells:
        for cell in row:
            if not cell.clicked:
                moves.append(cell)
    return moves

def alphabeta(cells, depth, alpha, beta, ai_turn):
    # Check if there is a winner or if the maximum depth is reached
    winner = check_winner()  # Came from functions.game
    if winner or depth == 0:
        return evaluate(winner, depth)  # Return the evaluation of the winner

    if ai_turn:
        # AI turn (maximizing player)
        max_eval = float('-inf')  # Initialize max evaluation with negative infinity
        for cell in get_possible_moves(cells):
            cell.click('O')  # Assume that AI is 'O'
            eval = alphabeta(cells, depth - 1, alpha, beta, False)  # Use recursion to call the next turn
            cell.clicked = False  # Reset state of the cell
            cell.symbol = None  # Reset the symbol of the cell
            max_eval = max(max_eval, eval)  # Update the maximum evaluation
            alpha = max(alpha, eval)  # Update the value of alpha
            if beta <= alpha:
                break  # Alpha-beta pruning: stop the search if the condition is met
        return max_eval  # Return the maximum evaluation
    else:
        # Opponent's turn (minimizing player)
        min_eval = float('inf')  # Initialize min evaluation with positive infinity
        for cell in get_possible_moves(cells):
            cell.click('X')  # Assume that 'X' is the opponent's symbol
            eval = alphabeta(cells, depth - 1, alpha, beta, True)  # Call recursively for the next turn
            cell.clicked = False  # Reset state of the cell
            cell.symbol = None  # Reset the symbol of the cell
            min_eval = min(min_eval, eval)  # Update the minimum evaluation
            beta = min(beta, eval)  # Update the value of beta
            if beta <= alpha:
                break  # Alpha-beta pruning: stop the search if the condition is met
        return min_eval  # Return the minimum evaluation
    
def evaluate(winner, depth):
    if winner == 'O':  # Assume that 'O' is the AI
        return 10 - depth  # Return a higher value if AI wins quickly
    elif winner == 'X':  # Assume that 'X' is the opponent
        return depth - 10  # Return a lower value if the opponent wins quickly
    else:
        return 0  # Return 0 if it is a draw

