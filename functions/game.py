import pygame
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

print(cells)
print(cell_row)