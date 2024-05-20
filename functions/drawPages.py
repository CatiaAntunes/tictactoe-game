import pygame
screen = pygame.display.set_mode((1280, 720))
from theme.elements import *

""" Draw the Main Page """
def draw_main_page(mousePos, mainButtons, mainButtonImages):
    #Fills the screen with the color salmon
    screen.fill(salmon)
    # Draws specified labels at their respective positions
    screen.blit(titleLb, titleLbRect)
    screen.blit(titleDescLb, titleDescLbRect)
    screen.blit(userOptionLb, userOptionLbRect)
    screen.blit(userOptionDescLb, userOptionDescLbRect)

    # Iterates over 'mainButtons' to draw the buttons. If the mouse cursor is over a button, it draws the hover image, otherwise, it draws the normal image
    for index, button in enumerate(mainButtons):
        normalImage, hoverImage = mainButtonImages[index]
        if button.collidepoint(mousePos):
            screen.blit(hoverImage, button.topleft)
        else:
            screen.blit(normalImage, button.topleft)

    # Updates the display with the drawn content
    pygame.display.flip()

""" Draw the Algorithm Selection Page """
def draw_algorithm_page(mousePos, algorithmButtons, algorithmButtonsImages):
    #Fills the screen with the color salmon
    screen.fill(salmon)
    # Draws specified labels at their respective positions
    screen.blit(titleLb, titleLbRect)
    screen.blit(titleDescLb, titleDescLbRect)
    screen.blit(algoOptionLb, algoOptionLbRect)
    screen.blit(algoOptionDescLb, algoOptionDescLbRect)
    # Iterates over 'algorithmButtons' to draw the buttons. If the mouse cursor is over a button, it draws the hover image, otherwise, it draws the normal image
    for index, button in enumerate(algorithmButtons):
        normalImage, hoverImage = algorithmButtonsImages[index]
        if button.collidepoint(mousePos):
            screen.blit(hoverImage, button.topleft)
        else:
            screen.blit(normalImage, button.topleft)
    
    # Updates the display with the drawn content
    pygame.display.flip()

""" Draw the Confirm Page """
def draw_confirm_page(mousePos, confirmButton, confirmButtonImages, adversary, algorithm, robotv2Images):
    # Gets choices made from the main page to display in a label, dynamically; Also gets the position (rect) information
    confirmOptionLb = get_confirmOptionLb(adversary, algorithm)
    confirmOptionLbRect = get_confirmOptionLb_rect(confirmOptionLb)
    #Fills the screen with the color salmon
    screen.fill(salmon)
    # Draws specified labels at their respective positions
    screen.blit(titleLb, titleLbRect)
    screen.blit(titleDescLb, titleDescLbRect)
    screen.blit(confirmOptionLb, confirmOptionLbRect)
    screen.blit(bipLb, bipLbRect)
    # Gets images for the robot image (not buttons)
    robotNormalImg, robotHoverImg = robotv2Images[0]
    screen.blit(robotNormalImg, (500, 350))
    # Iterates over 'confirmButtons' to draw the buttons. If the mouse cursor is over the YES button, it draws the hover image, otherwise, it draws the normal image
    for index, button in enumerate(confirmButton):
        normalImage, hoverImage = confirmButtonImages[index]
        if button.collidepoint(mousePos):
            screen.blit(hoverImage, button.topleft)
            if index == 0:
                screen.blit(robotHoverImg, (500, 350))
            else:
                screen.blit(robotNormalImg, (500, 350))
        else:
            screen.blit(normalImage, button.topleft)
    
    # Updates the display with the drawn content
    pygame.display.flip()

""" Draw the Game Page """
def draw_game_page(mousePos, gameBoard):
    #Fills the screen with the color salmon
    screen.fill(salmon)
    # Draws specified labels at their respective positions
    titleLbRect = titleLb.get_rect(center=(150, 50))
    titleDescLbRect = titleDescLb.get_rect(center=(220,70))
    screen.blit(titleLb, titleLbRect)
    screen.blit(titleDescLb, titleDescLbRect)
    # Draws the gameBoard
    screen.blit(gameBoard, (325,50))

    # Updates the display with the drawn content
    pygame.display.flip()
