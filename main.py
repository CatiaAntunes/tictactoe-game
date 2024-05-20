import pygame
import sys
import time
from functions.drawPages import draw_algorithm_page, draw_confirm_page, draw_main_page, draw_game_page
from functions.game import cells, draw_game_board, check_winner, Cell
from theme.elements import description
from algorithms.minmax import minmax
from algorithms.alphabeta import alphabeta
import random
import tracemalloc

# Functions to get Adversary and Algorithm
def get_adversary():
    return adversary

def get_algorithm():
    return algorithm

def display_top(snapshot):
    top_stats = snapshot.statistics('lineno')
    #print("[ Top 10 Memory Consuming Lines ]")
    for stat in top_stats[:10]:
        print(stat)
    print('')

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Import after pygame display, otherwise it does not have an active display surface when it tries to convert the images
from theme.imagesButtons import *

# Game state
#  control game loop
running = True
#  tracks the current page being displayed
currentPage = 'main'
# tracks the current hovered button
hoveredButton = None
# variables to store the clicked button and the selected adversay and algorithm
buttonClicked, adversary, algorithm = '', '', ''
# Flag to indicate if the game's over
gameOver = False

# List of choices for buttons on different pages, to be mapped inside the Button Click Check functions
mainButtonChoices = ["Human", "Robot"]
algorithmButtonChoices = ["AlphaBeta", "MinMax"]
confirmButtonChoices = ["Yes", "No"]

""" Button Click Functions 
Used in the main game loop to check whether a button has been clicked and what to do after
Main Check Button Click = To control when a button of the main buttons is clicked, leading to next page and saving button clicked to later use (adversary)
Algorithm Check Button Click = To control when a button of the algorithm buttons is clicked, leading to next page and saving button clicked to later use (algorithm)
Confirm Check Button Click = To control when a button of the confirm buttons is clicked, leading to the game or returning to main page
"""

def main_check_button_click(pos):
    # with global, we're saying that these variables inside the function refer to the global variables defined outside this function
    global currentPage, buttonClicked
    for index, button in enumerate(mainButtons):
        if button.collidepoint(pos):
            # Regardless of the choice, it goes to next page, which we defined is the confirm page
            currentPage = 'algorithm'
            # We know before that, for example, the first button in mainButtons (from imagesButtons.py) refers to the first button in mainButtonChoices (main.py) and so on
            buttonClicked = mainButtonChoices[index]
            return True
    return False

def algorithm_check_button_click(pos):
    # refer to the global variables defined outside this function
    global currentPage, buttonClicked
    for index, button in enumerate(algorithmButtons):
        if button.collidepoint(pos):
            # Regardless of the choice, it goes to next page, which we defined is the confirm page
            currentPage = 'confirm'
            # We know before that, for example, the first button in algorithmButtons (from imagesButtons.py) refers to the first button in algorithmButtonChoices (main.py) and so on
            buttonClicked = algorithmButtonChoices[index]
            return True
    return False

def confirm_check_button_click(pos):
    # refer to the global variables defined outside this function
    global currentPage, buttonClicked
    for index, button in enumerate(confirmButtons):
        if button.collidepoint(pos):
            # We know before that, for example, the first button in confirmButtons (from imagesButtons.py) refers to the first button in confirmButtonChoices (main.py) and so on
            buttonClicked = confirmButtonChoices[index]
            return True
    return False

firstMoveDone = False
def click_randomCell():
    global updateDisplay
    available_cells = [cell for row in cells for cell in row if not cell.clicked]
    if available_cells:
        randomCell = random.choice(available_cells)
        randomCell.click(currentSymbol)
        updateDisplay = True
        print("First random cell clicked")
        return True
    return False

""" Game Setup """
# List of Players and mapping of their symbols
players = ['BIP', 'Adversary']
playerSymbols = {'X': 'Adversary', 'O': 'BIP'}

# Removed random first player because we assigned harcoded that the 'Adversary' is the first player and gets the 'X'
#  to improve: get the first player randomly and assign 'X' to it
#random.shuffle(players)

# First player is the second place in the list ('Adversary')
currentPlayer = players[1]

# Sets the current symbol to control later on which symbol to draw ingame
currentSymbol = 'X'

# Statistics - Initialize number of moves (to know later on how many moves were made)
numMoves = 0
# Statistics - Tracks the time of the last move (to know later on how long does it take for the AI to play)
lastMoveTime = pygame.time.get_ticks()
# Move Delay = used to see the plays without being too fast and closing the game immediately
moveDelay = 1500

""" Make Robot Move 
Handles the logic for the AI to make a move
"""
def make_robot_move():
    # Gets variables defined outside of the function
    global currentSymbol, updateDisplay, lastMoveTime, currentPlayer, numMoves
    # Gets the symbol of the current player
    symbol = currentSymbol
    # Saves next symbol and player for when a play ends
    nextSymbol = 'O' if currentSymbol == 'X' else 'X'
    nextPlayer = 'BIP' if currentPlayer == 'Adversary' else 'Adversary'

    # Initializes timing and best move tracking
    tracemalloc.start()
    startTime = time.perf_counter_ns()
    bestScore = float('-inf')
    bestMove = None

    # Evaluates each cell
    for row in cells:
        for cell in row:
            # If a cell is not clicked, simulate a click
            if not cell.clicked:

                cell.click(symbol)
                # Uses the algorithm based on the current player and selected algorithm
                if ((algorithm == 'MinMax' and currentPlayer == 'BIP') or (algorithm == 'AlphaBeta' and currentPlayer == 'Adversary')):
                    score = minmax(cells, 5, False)
                else:
                    score = alphabeta(cells, 5, float('-inf'), float('inf'), False)
                # Resets the cell after evaluation
                cell.clicked = False
                cell.symbol = None
                # Tracks the best move based on the score
                if score > bestScore:
                    bestScore = score
                    bestMove = cell
    # Make the best move, if found
    if bestMove:
        bestMove.click(symbol)
        # Updates game state variables
        currentSymbol = nextSymbol
        currentPlayer = nextPlayer
        updateDisplay = True

        # Updates statistic variables
        lastMoveTime = pygame.time.get_ticks()  # Update last move time
        endTime = time.perf_counter_ns()  # Get end time
        elapsed_time_ns = endTime - startTime
        numMoves += 1
        
        # Show time spent by AI move with 4 decimal places and avoid "0.0"
        elapsed_time_us = elapsed_time_ns / 1_000  # Convert nanoseconds to microseconds
        elapsed_time_s = elapsed_time_ns / 1_000_000_000
        player = 'BIP' if symbol == 'O' else 'Robot'
        if elapsed_time_ns > 100:  # Check if time is greater than 100 nanoseconds
            print(f"Move {numMoves} by {player}: Time Spent: {elapsed_time_s:.4f} seconds ({elapsed_time_us:.0f} microseconds)")
        else:
            print(f"Move {numMoves}: Time Spent: < 0.0001 seconds (< 100 microseconds)")

        snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()
        display_top(snapshot)


# Function responsible for displaying which player turn is it
#  Only showing images and not text. To improve
def draw_current_turn():
    left_side_img_coord = (100, 350)
    right_side_img_coord = (1100, 350)

    if currentPlayer == 'BIP':
        bip_text = description.render("BIP's turn", True, (0, 0, 0))
        bip_img = imgBipGame
        adversary_img = imgHumanFadedGame if adversary == 'Human' else imgRobotFadedGame
    else:
        bip_img = imgBipFadedGame
        adversary_img = imgHumanGame if adversary == 'Human' else imgRobotGame

    bip_img_rect = bip_img.get_rect(center=left_side_img_coord)
    screen.blit(bip_img, bip_img_rect)

    adversary_img_rect = adversary_img.get_rect(center=right_side_img_coord)
    screen.blit(adversary_img, adversary_img_rect)

""" Main Game Loop """
while running:
    # Tracks the current mouse position
    mouse_pos = pygame.mouse.get_pos()
    # Flag to indicate if the display needs updating
    updateDisplay = False
    # Tracks the current time in milliseconds
    currentTime = pygame.time.get_ticks()
    # Event Handling
    for event in pygame.event.get():
        # Quit Event to Stop the Game
        if event.type == pygame.QUIT:
            running = False
        # Mouse button down event to handle clicks on different pages and game interactions
        if not gameOver and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Handles main page button clicks and changes; also logs which pages has been clicked
                if currentPage == 'main' and main_check_button_click(event.pos):
                    print(f"Button {buttonClicked} clicked")
                    adversary = buttonClicked
                    updateDisplay = True
                # Handles algorithm page button clicks and changes; also logs which pages has been clicked
                elif currentPage == 'algorithm' and algorithm_check_button_click(event.pos):
                    print(f"Button {buttonClicked} clicked")
                    algorithm = buttonClicked
                    updateDisplay = True
                # Handles confirm page button clicks and changes; also logs which pages has been clicked
                elif currentPage == 'confirm' and confirm_check_button_click(event.pos):
                    print(f"Button {buttonClicked}")
                    print(f"Button {buttonClicked} clicked")
                    # If user clicks yes, it proceeds to game
                    if buttonClicked == 'Yes':
                        currentPage = 'game'
                    # otherwise, it goes back to the main page and resets user choices up until this point
                    else:
                        currentPage = 'main'
                        adversary, algorithm = '', ''
                    updateDisplay = True
                # Handles game page interactions, when it's the Human playing (for user input) - for others there's no need to check for mouse input, for example
                elif currentPage == 'game' and adversary == 'Human' and currentPlayer == 'Adversary':
                    for row in cells:
                        for cell in row:
                            if cell.rect.collidepoint(event.pos) and not cell.clicked:
                                if cell.click(currentSymbol):
                                    currentSymbol = 'O' if currentSymbol == 'X' else 'X'
                                    currentPlayer = 'BIP'
                                    updateDisplay = True
                                    lastMoveTime = pygame.time.get_ticks()  # Update last move time
    # If we're in game and it is not the Human playing, but BIP or the Robot, make_robot_move()
    if not gameOver and currentPage == 'game':
        if adversary == 'Human' and currentPlayer == 'BIP' and currentTime - lastMoveTime > moveDelay:
            make_robot_move()
        elif adversary == 'Robot' and currentTime - lastMoveTime > moveDelay:
            if not firstMoveDone:
                click_randomCell()
                firstMoveDone = True
                lastMoveTime = pygame.time.get_ticks()  # Update last move time after the first random move
                currentSymbol = 'O' if currentSymbol == 'X' else 'X'
                currentPlayer = 'BIP'
            else:
                make_robot_move()

    # Checks if there's a winner and prints the results on the console
    winner = check_winner()
    if winner:
        if winner == 'Draw':
            print("It's a draw!")
        else:
            winner_name = 'BIP' if winner == 'O' else 'Adversary'
            if winner_name == 'Adversary':
                winner_name = 'Human' if adversary == 'Human' else 'Robot'
            print(f"Player {winner_name} wins!")
        running = False
        # Set gameOver to True to indicate the game has ended
        gameOver = True
        

    # Page drawing, based on current page
    if currentPage == 'main':
        draw_main_page(mouse_pos, mainButtons, mainButtonImages)
    elif currentPage == 'algorithm':
        draw_algorithm_page(mouse_pos, algorithmButtons, algorithmButtonImages)
    elif currentPage == 'confirm':
        draw_confirm_page(mouse_pos, confirmButtons, confirmButtonImages, adversary, algorithm, robotv2Images)
    elif currentPage == 'game':
        if updateDisplay:
            draw_game_page(mouse_pos, imgGameBoard)
            draw_game_board()
            draw_current_turn()
            pygame.display.flip()

    if currentPage != 'game':
        pygame.display.flip()

    clock.tick(60)  # Limit the frame rate to 60 FPS


# Keep the window open after the game ends
while gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False

pygame.quit()
