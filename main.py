import pygame
import sys
from functions.drawPages import draw_algorithm_page, draw_confirm_page, draw_main_page, draw_game_page
from functions.game import *

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
current_page = 'main'
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

players = ['BIP', 'Adversary'] 
random.shuffle(players)
current_player = players[0]
current_symbol = 'X'
last_move_time = pygame.time.get_ticks()
move_delay = 1000
player_symbols = {'X': current_player, 'O': 'BIP' if current_player == 'Adversary' else 'Adversary'}


def make_robot_move():
    global current_symbol, update_display, last_move_time, current_player
    available_cells = [cell for row in cells for cell in row if not cell.clicked]
    if available_cells:
        cell = random.choice(available_cells)
        cell.click(current_symbol)
        current_symbol = 'O' if current_symbol == 'X' else 'X'
        current_player = 'Adversary' if current_player == 'BIP' else 'BIP'
        update_display = True
        last_move_time = pygame.time.get_ticks()

while running:
    mouse_pos = pygame.mouse.get_pos()
    update_display = False
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if current_page == 'main' and main_check_button_click(event.pos):
                    print(f"Button {button_clicked} clicked")
                    adversary = button_clicked
                    update_display = True
                    
                elif current_page == 'algorithm' and algorithm_check_button_click(event.pos):
                    print(f"Button {button_clicked} clicked")
                    algorithm = button_clicked
                    update_display = True
                
                elif current_page == 'confirm' and confirm_check_button_click(event.pos):
                    print(f"Button {button_clicked} clicked")
                    if button_clicked == 'Yes':
                        current_page = 'game'
                    else:
                        current_page = 'main'
                        adversary, algorithm = '', ''
                    update_display = True
                elif current_page == 'game':
                    if adversary == 'Human' and current_player == 'Adversary':
                        for row in cells:
                            for cell in row:
                                if cell.rect.collidepoint(event.pos):
                                    if cell.click(current_symbol):
                                        current_symbol = 'O' if current_symbol == 'X' else 'X'
                                        current_player = 'BIP'
                                        update_display = True
                                        last_move_time = pygame.time.get_ticks()  # Update last move time

    if current_page == 'game':
        if adversary == 'Human' and current_player == 'BIP' and current_time - last_move_time > move_delay:
            make_robot_move()
        elif adversary == 'Robot' and current_time - last_move_time > move_delay:
            make_robot_move()

    winner = check_winner()
    if winner:
        if winner == 'Draw':
            print("It's a draw!")
        else:
            winner_name = player_symbols[winner]
            if winner_name == 'Adversary':
                winner_name = 'Human' if adversary == 'Human' else 'Robot'
            print(f"Player {winner_name} wins!")
        running = False

    if current_page == 'main':
        draw_main_page(mouse_pos, main_buttons, main_button_images)
    elif current_page == 'algorithm':
        draw_algorithm_page(mouse_pos, algorithm_buttons, algorithm_button_images)
    elif current_page == 'confirm':
        draw_confirm_page(mouse_pos, confirm_buttons, confirm_button_images, adversary, algorithm, robotv2_images)
    elif current_page == 'game':
        if update_display:
            screen.fill((255, 255, 255))
            draw_game_page(mouse_pos, imgGameBoard)
            draw_game_board()
            pygame.display.flip()

    if current_page != 'game':
        pygame.display.flip()

    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()
