import pygame
import sys
from theme.elements import *
from functions.drawPages import *

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Import after pygame display, otherwise it does not have an active display surface when it tries to convert the images
from theme.imagesButtons import *

# Game state
running = True
current_page = 'main'
hovered_button = None

def main_check_button_click(pos):
    global current_page
    for index, button in enumerate(main_buttons):
        if button.collidepoint(pos):
            current_page = f'page_{index + 1}'
            return True
    return False

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if current_page == 'main' and main_check_button_click(event.pos):
                    print(f"Button {current_page} clicked")

    if current_page == 'main':
        draw_main_page(mouse_pos, main_buttons, main_button_images)
    elif current_page == 'page_1':
        draw_algorithm_page(mouse_pos, algorithm_buttons, algorithm_button_images)
        # Additional functionality here
        pygame.display.flip()
    elif current_page == 'page_2':
        draw_algorithm_page(mouse_pos, algorithm_buttons, algorithm_button_images)
        # Handle drawing for page 2
        screen.fill(white)
        # Additional functionality here
        pygame.display.flip()

    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()
