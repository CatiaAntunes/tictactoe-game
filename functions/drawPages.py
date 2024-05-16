import pygame
screen = pygame.display.set_mode((1280, 720))
from theme.elements import *

def draw_main_page(mouse_pos, main_buttons, main_button_images):
    screen.fill(salmon)
    screen.blit(titleLb, titleLb_rect)
    screen.blit(titleDescLb, titleDescLb_rect)
    screen.blit(userOptionLb, userOptionLb_rect)
    screen.blit(userOptionDescLb, userOptionDescLb_rect)
    for index, button in enumerate(main_buttons):
        normal_image, hover_image = main_button_images[index]
        if button.collidepoint(mouse_pos):
            screen.blit(hover_image, button.topleft)
        else:
            screen.blit(normal_image, button.topleft)
    pygame.display.flip()

def draw_algorithm_page(mouse_pos, algorithm_buttons, algorithm_button_images):
    screen.fill(salmon)
    screen.blit(titleLb, titleLb_rect)
    screen.blit(titleDescLb, titleDescLb_rect)
    screen.blit(algoOptionLb, algoOptionLb_rect)
    screen.blit(algoOptionDescLb, algoOptionDescLb_rect)
    for index, button in enumerate(algorithm_buttons):
        normal_image, hover_image = algorithm_button_images[index]
        if button.collidepoint(mouse_pos):
            screen.blit(hover_image, button.topleft)
        else:
            screen.blit(normal_image, button.topleft)
    pygame.display.flip()

def draw_confirm_page(mouse_pos, confirm_button, confirm_button_images, adversary, algorithm, robotv2_images):
    confirmOptionLb = get_confirmOptionLb(adversary, algorithm)
    confirmOptionLb_rect = get_confirmOptionLb_rect(confirmOptionLb)
    screen.fill(salmon)
    screen.blit(titleLb, titleLb_rect)
    screen.blit(titleDescLb, titleDescLb_rect)
    screen.blit(confirmOptionLb, confirmOptionLb_rect)
    screen.blit(bipLb, bipLb_rect)
    robot_normal_img, robot_hover_img = robotv2_images[0]
    screen.blit(robot_normal_img, (500, 350))
    for index, button in enumerate(confirm_button):
        normal_image, hover_image = confirm_button_images[index]
        if button.collidepoint(mouse_pos):
            screen.blit(hover_image, button.topleft)
            if index == 0:
                screen.blit(robot_hover_img, (500, 350))
            else:
                screen.blit(robot_normal_img, (500, 350))
        else:
            screen.blit(normal_image, button.topleft)
    pygame.display.flip()

def draw_game_page(mouse_pos, game_board):
    screen.fill(salmon)
    titleLb_rect = titleLb.get_rect(center=(150, 50))
    titleDescLb_rect = titleDescLb.get_rect(center=(220,70))
    screen.blit(titleLb, titleLb_rect)
    screen.blit(titleDescLb, titleDescLb_rect)
    screen.blit(game_board, (325,50))
    

    pygame.display.flip()
