import pygame
pygame.init()

imgHuman = pygame.image.load('img/icons8-human-head-256.png').convert_alpha()
imgHumanHover = pygame.image.load('img/icons8-human-head-256-hover.png').convert_alpha()

imgRobot = pygame.image.load('img/icons8-r2-d2-256.png').convert_alpha()
imgRobotHover = pygame.image.load('img/icons8-r2-d2-256-hover.png').convert_alpha()

imgRobotv2 = pygame.image.load('img/icons8-bmo-256.png').convert_alpha()
imgRobotv2Hover = pygame.image.load('img/icons8-bmo-256-hover.png').convert_alpha()

imgAlphaBeta = pygame.image.load('img/alphabeta.png').convert_alpha()
imgAlphaBetaHover = pygame.image.load('img/alphabeta-hover.png').convert_alpha()

imgMinMax = pygame.image.load('img/minmax.png').convert_alpha()
imgMinMaxHover = pygame.image.load('img/minmax-hover.png').convert_alpha()

# Button setup
btHuman = pygame.Rect(250, 250, imgHuman.get_width(), imgHumanHover.get_height())
btRobot = pygame.Rect(789, 250, imgRobot.get_width(), imgRobotHover.get_height())
main_buttons = [btHuman, btRobot]

btalphabeta = pygame.Rect(250, 250, imgAlphaBeta.get_width(), imgAlphaBetaHover.get_height())
btminmax = pygame.Rect(789, 250, imgMinMax.get_width(), imgMinMaxHover.get_height())
algorithm_buttons = [btalphabeta, btminmax]

main_button_images = [
    (imgHuman, imgHumanHover),
    (imgRobot, imgRobotHover)
]

algorithm_button_images = [
    (imgAlphaBeta, imgAlphaBetaHover),
    (imgMinMax, imgMinMaxHover)
]