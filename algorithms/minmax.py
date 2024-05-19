from functions.game import *

""" Get Possible Moves Function
This function iterates through all the cells in the tic-tac-toe board and returns a list of cells that have not been clicked. 
These are the possible moves that can be made in the current state of the game.
"""
def get_possible_moves(cells):
    moves = []
    for row in cells:
        for cell in row:
            if not cell.clicked:
                moves.append(cell)
    return moves

""" MinMax Algorithm Function
1. The algorithm first checks if there's a winner or if the maximum depth (search limit) has been reached
2. Depending on whose turn it is ('ai turn'), the function recursively evaluates all possible moves
"""

def minmax(cells, depth, ai_turn):
    winner = check_winner()
    if winner or depth == 0:
        return evaluate(winner)

    """ AI's Turn"""
    if ai_turn:
        # Initialize max_eval to negative infinity
        max_eval = float('-inf')
        for cell in get_possible_moves(cells):
            # Simulate by clicking the cell with 'O'
            cell.click('O')
            # Recursively call minmax with decreased depth and 'ai_turn' set to False
            eval = minmax(cells, depth - 1, False)
            # Undo the move by resetting the cell's clicked status and symbol
            cell.clicked = False
            cell.symbol = None
            #Update max_eval with the maximum value between max_eval and the evaluation of the move
            max_eval = max(max_eval, eval)
        # Return max_eval    
        return max_eval
    
    # Minimizing Player's Turn
    else:
        # Initialize 'min_eval' to positive infinity
        min_eval = float('inf')
        # For each possible move
        for cell in get_possible_moves(cells):
            # Simulate the move by clicking the cell with 'X'
            cell.click('X') 
            # Recursively call 'minmax' with decreased depth and 'ai turn' set to True
            eval = minmax(cells, depth - 1, True)
            # Undo the move by resetting the cell's clicked status and symbol
            cell.clicked = False
            cell.symbol = None
            # Update min_eval with the minimum value between 'min_eval' and the evaluation of the move
            min_eval = min(min_eval, eval)
        # Return min_eval
        return min_eval

""" Evaluate Function
This function returns a score based on the winner
1 if 'O' wins = AI
-1 if 'X' wins = Human
0 if there's no winner (draw or ongoing game)
"""
def evaluate(winner):
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    else:
        return 0

""" To Improve
The symbols 'X' and 'O' are harcoded for the AI and Human Players. It should follow main.py logic
"""