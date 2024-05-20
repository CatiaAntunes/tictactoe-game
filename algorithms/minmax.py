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
def minmax(cells, depth, aiTurn):
    winner = check_winner()
    if winner or depth == 0:
        return evaluate(winner)

    """ AI's Turn"""
    if aiTurn:
        # Initialize maxEval to negative infinity
        maxEval = float('-inf')
        for cell in get_possible_moves(cells):
            # Simulate by clicking the cell with 'O'
            cell.click('O')
            # Recursively call minmax with decreased depth and 'aiTurn' set to False
            eval = minmax(cells, depth - 1, False)
            # Undo the move by resetting the cell's clicked status and symbol
            cell.clicked = False
            cell.symbol = None
            #Update maxEval with the maximum value between maxEval and the evaluation of the move
            maxEval = max(maxEval, eval)
        # Return maxEval    
        return maxEval
    
    # Minimizing Player's Turn
    else:
        # Initialize 'minEval' to positive infinity
        minEval = float('inf')
        # For each possible move
        for cell in get_possible_moves(cells):
            # Simulate the move by clicking the cell with 'X'
            cell.click('X') 
            # Recursively call 'minmax' with decreased depth and 'ai turn' set to True
            eval = minmax(cells, depth - 1, True)
            # Undo the move by resetting the cell's clicked status and symbol
            cell.clicked = False
            cell.symbol = None
            # Update minEval with the minimum value between 'minEval' and the evaluation of the move
            minEval = min(minEval, eval)
        # Return minEval
        return minEval

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