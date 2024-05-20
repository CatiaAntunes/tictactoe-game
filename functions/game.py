import pygame
from theme.imagesButtons import imgGameCircle, imgGameCross

screen = pygame.display.set_mode((1280, 720))

""" Cell Class 
Represents a single cell in the game board grid
"""
class Cell:
    """ Initialization 
        self.rect = object defining the cell's position and size
        self.clicked = boolean indicating whether the cell has been clicked
        self.symbol = stores the symbol ('X' or 'O') that occupies the cell
        row and col added for debugging purposes
    """
    def __init__(self, x, y, width, height, row, col):
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False
        self.symbol = None
        self.row = row
        self.col = col

    """ Click Method 
        Updates the cell's state to the given symbol if it has not been clicked yet
    """
    def click(self, symbol):
        # If it has not been clicked
        if not self.clicked:
            # Assign the symbol of the current player
            self.symbol = symbol
            # Changes the clicked to True
            self.clicked = True
            #print(f"Cell clicked at position ({self.row + 1}, {self.col + 1}) with symbol {symbol}") #debug
            return True
        # Otherwise returns False (so it cannot be clicked)
        return False
    
    """ Draw Method 
        Draws the appropriated symbol (circle or cross) on the screen based on the cell's state
    """
    def draw(self, screen):
        # Depending on the player's symbol
        if self.symbol == 'X':
            # Rectangle used to position the symbol image
            imgRect = imgGameCross.get_rect(center=self.rect.center)
            # Draws the image on the screen, at that position
            screen.blit(imgGameCross, imgRect.topleft)
        elif self.symbol == 'O':
            # Rectangle used to position the symbol image
            imgRect = imgGameCircle.get_rect(center=self.rect.center)
            # Draws the image on the screen, at that position
            screen.blit(imgGameCircle, imgRect.topleft)

# Setting Up the Game Board
cells = []
cellSize = 190
margin = 10
startX = 330
startY = 55

# Create a 3x3 grid of 'Cell' objects
for row in range(3):
    cellRow = []
    for col in range(3):
        x = startX + col * (cellSize + margin)
        y = startY + row * (cellSize + margin)
        cellRow.append(Cell(x, y, cellSize, cellSize, row, col))
    cells.append(cellRow)

""" Draw Game Board
Iterates over all the cells and calls their draw method to render them on screen
"""
def draw_game_board():
    for row in cells:
        for cell in row:
            cell.draw(screen)

""" Checking for a Winner
This function determines it there is a winner  or if the game is a draw
Checks all rows, columns and diagonals for three matching symbols
"""
def check_winner():
    # Check rows
    for row in cells:
        if row[0].symbol == row[1].symbol == row[2].symbol and row[0].symbol is not None:
            return row[0].symbol

    # Check columns
    for col in range(3):
        if cells[0][col].symbol == cells[1][col].symbol == cells[2][col].symbol and cells[0][col].symbol is not None:
            return cells[0][col].symbol

    # Check diagonals
    if cells[0][0].symbol == cells[1][1].symbol == cells[2][2].symbol and cells[0][0].symbol is not None:
        return cells[0][0].symbol
    if cells[0][2].symbol == cells[1][1].symbol == cells[2][0].symbol and cells[0][2].symbol is not None:
        return cells[0][2].symbol

    # Check for draw
        # all function takes and iterable and returns True if all elements of the iterable are True. Otherwise, it returns False
    if all(cell.clicked for row in cells for cell in row):
        return "Draw"

    return None