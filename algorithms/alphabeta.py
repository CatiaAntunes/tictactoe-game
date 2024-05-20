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

""" Alpha-Beta Algorithm
This function implements the Alpha-Beta Algorithm
1. The algorithm first checks if there's a winner or if the maximum search depth has been reached
2. Depending on whose turn it is ('ai turn'), the function recursively evaluates all possible moves
"""
def alphabeta(cells, depth, alpha, beta, aiTurn):
    # Checks if there's a winner
    winner = check_winner()
    # If that turns out to be true or depth has reached 0 (no more possible moves)
    if winner or depth == 0:
        # Returns the evaluation of the board state using the evaluate function
        return evaluate(winner, depth)
    
    """ AI's Turn """
    # Maximizing AI's Turn
    if aiTurn:
        # Initialize 'maxEval' to negative infinity
        maxEval = float('-inf')
        # For each possible move
        for cell in get_possible_moves(cells):
            # Simulate the move by clicking the cell with 'O'
            cell.click('O') 
            # Recursively call 'alphabeta' with decreased depth, updated alpha and beta values and aiTurn
            eval = alphabeta(cells, depth - 1, alpha, beta, False)
            # Undo the move by resetting the cell's clicked and symbol
            cell.clicked = False
            cell.symbol = None
            # Update 'maxEval' with the maximum value between maxEval and evaluation of the move
            maxEval = max(maxEval, eval)
            # Update alpha with the maximum value between 'alpha' and 'eval'
            alpha = max(alpha, eval)
            # If beta is less than or equal to alpha, break out of the loop (prunning)
            if beta <= alpha:
                break
        # Return 'maxEval'
        return maxEval
    
    # Minimizing Player's Turn
    else:
        # Initialize 'minEval' to positive infinity
        minEval = float('inf')
        # For each possible move
        for cell in get_possible_moves(cells):
            # Simulate the move by clicking the cell with 'X'
            cell.click('X')
            # Recursively call 'alphabeta' with decreased depth, updated alpha and beta values, and sets 'aiTurn' to True
            eval = alphabeta(cells, depth - 1, alpha, beta, True)
            # Undo the move by resetting the cell's clicked and symbol
            cell.clicked = False
            cell.symbol = None
            # Update 'minEval' with the minimum value between 'minEval' and the evaluation of the move
            minEval = min(minEval, eval)
            # Update beta with the minimum value between value and eval
            beta = min(beta, eval)
            # If beta is less than or equal to 'alpha', break out of the loop (prunning)
            if beta <= alpha:
                break
        # Return 'minEval'
        return minEval

""" Evaluate Function
The evaluate function returns a score based on the winner and the depth
10 - depth if 'O' wins = the faster the win, the higher the score
depth - 10 if 'X' wins = the faster the loss, the lower the score
'0' if there's no winner (draw or ongoing game)
"""    
def evaluate(winner, depth):
    if winner == 'O':
        return 10 - depth
    elif winner == 'X':
        return depth - 10
    else:
        return 0

