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
    for index, button in enumerate(algorithm_buttons):
        normal_image, hover_image = algorithm_button_images[index]
        if button.collidepoint(mouse_pos):
            screen.blit(hover_image, button.topleft)
        else:
            screen.blit(normal_image, button.topleft)
    pygame.display.flip()