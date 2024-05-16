import pygame
import sys
from functions.drawPages import draw_algorithm_page, draw_confirm_page, draw_main_page, draw_game_page

def get_adversary():
    return adversary

def get_algorithm():
    return algorithm


# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Import after pygame display, otherwise it does not have an active display surface when it tries to convert the images
from theme.imagesButtons import *

# Game state
running = True
current_page = 'game'
hovered_button = None
button_clicked, adversary, algorithm = '', '', ''

main_button_choices = ["Human", "Robot"]
algorithm_button_choices = ["AlphaBeta", "MinMax"]
confirm_button_choices = ["Yes", "No"]

def main_check_button_click(pos):
    global current_page, button_clicked
    for index, button in enumerate(main_buttons):
        if button.collidepoint(pos):
            current_page = 'algorithm'
            button_clicked = main_button_choices[index]
            return True
    return False

def algorithm_check_button_click(pos):
    global current_page, button_clicked
    for index, button in enumerate(algorithm_buttons):
        if button.collidepoint(pos):
            current_page = 'confirm'
            button_clicked = algorithm_button_choices[index]
            return True
    return False

def confirm_check_button_click(pos):
    global current_page, button_clicked
    for index, button in enumerate(confirm_buttons):
        if button.collidepoint(pos):
            button_clicked = confirm_button_choices[index]
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
                    print(f"Button {button_clicked} clicked")
                    adversary = button_clicked
                    
                elif current_page == 'algorithm' and algorithm_check_button_click(event.pos):
                    print(f"Button {button_clicked} clicked")
                    algorithm = button_clicked
                
                elif current_page == 'confirm' and confirm_check_button_click(event.pos):
                    print(f"Button {button_clicked} clicked")
                    if button_clicked == 'Yes':
                        current_page = 'game'
                    else:
                        current_page = 'main'
                        adversary, algorithm = '', ''

    if current_page == 'main':
        draw_main_page(mouse_pos, main_buttons, main_button_images)
    elif current_page == 'algorithm':
        draw_algorithm_page(mouse_pos, algorithm_buttons, algorithm_button_images)
    elif current_page == 'confirm':
        draw_confirm_page(mouse_pos, confirm_buttons, confirm_button_images, adversary, algorithm, robotv2_images)
    elif current_page == 'game':
        draw_game_page(mouse_pos, imgGameBoard)


    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()
