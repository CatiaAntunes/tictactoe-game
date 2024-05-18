from functions.game import *

def get_possible_moves(cells):
    # Function to return all possible moves (unclicked cells) on the board.
    moves = []
    for row in cells:
        for cell in row:
            if not cell.clicked:
                moves.append(cell)
                # print(moves)
    return moves

def alphabeta(cells, depth, alpha, beta, ai_turn):
    # Check of there is a winner or the maximum depth is reached
    winner = check_winner()  # Came from functions.game 
    if winner or depth == 0:
        return evaluate(winner)  # Return the evaluation of the winner

    if ai_turn:
        # AI turn (maximizing player)
        max_eval = float('-inf')  # Inicializa a avaliação máxima com negativo infinito # Retorna o valor mais baixo possível
        for cell in get_possible_moves(cells):
            cell.click('O')  # Assume that AI is 'O'
            eval = alphabeta(cells, depth - 1, alpha, beta, False)  # Use recursion to call the next turn
            cell.clicked = False  # Reset state of the cell
            cell.symbol = None  # Reset the symbol of the cell
            max_eval = max(max_eval, eval)  # Update the maximum evaluation
            alpha = max(alpha, eval)  # Update the value of alpha to max 
            if beta <= alpha:
                break  # Poda alfa-beta: interrompe a procura se a condição for satisfeita
        return max_eval  # Return the maximum evaluation
    else:
        # Bloco para a jogada do jogador adversário (minimizing player)
        min_eval = float('inf')  # Inicializa a avaliação mínima com positivo infinito
        for cell in get_possible_moves(cells):
            cell.click('X')  # Assume que 'X' é o símbolo do jogador adversário
            eval = alphabeta(cells, depth - 1, alpha, beta, True)  # Chama recursivamente para o próximo turno
            cell.clicked = False  # Reset state of the cella
            cell.symbol = None   # Reset the symbol of the cell
            min_eval = min(min_eval, eval)  # Update the minimum evaluation
            beta = min(beta, eval)  # Atualiza o valor de beta
            if beta <= alpha:
                break  # Poda alfa-beta: interrompe a procura se a condição for satisfeita
        return min_eval  # Return the minium evaluation

def evaluate(winner):
    if winner == 'O':  # Assume that 'O' is the AI
        return 1  # Return 1 if AI wins
    elif winner == 'X':  # Assume that 'X' is the opponent
        return -1  # return -1 if the opponent wins
    else:
        return 0  # Return 0 if it is a draw
