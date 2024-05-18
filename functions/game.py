import pygame
import random
import time
from theme.imagesButtons import imgGameCircle, imgGameCross

screen = pygame.display.set_mode((1280, 720))

class Cell:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False
        self.symbol = None

    def click(self, symbol):
        if not self.clicked:
            self.symbol = symbol
            self.clicked = True
            return True
        return False
    
    def draw(self, screen):
        if self.symbol == 'X':
            img_rect = imgGameCross.get_rect(center=self.rect.center)
            screen.blit(imgGameCross, img_rect.topleft)
        elif self.symbol == 'O':
            img_rect = imgGameCircle.get_rect(center=self.rect.center)
            screen.blit(imgGameCircle, img_rect.topleft)

cells = []
cell_size = 190
margin = 10
start_x = 330
start_y = 55

for row in range(3):
    cell_row = []
    for col in range(3):
        x = start_x + col * (cell_size + margin)
        y = start_y + row * (cell_size + margin)
        cell_row.append(Cell(x, y, cell_size, cell_size))
    cells.append(cell_row)

def draw_game_board():
    for row in cells:
        for cell in row:
            cell.draw(screen)

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
    if all(cell.clicked for row in cells for cell in row):
        return "Draw"

    return None