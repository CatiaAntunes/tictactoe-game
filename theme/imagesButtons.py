import pygame
pygame.init()

# Getting/Loading all images
imgHuman = pygame.image.load('img/icons8-human-head-256.png').convert_alpha()
imgHumanHover = pygame.image.load('img/icons8-human-head-256-hover.png').convert_alpha()
imgHumanFaded = pygame.image.load('img/icons8-human-head-256-faded.png').convert_alpha()

imgRobot = pygame.image.load('img/icons8-r2-d2-256.png').convert_alpha()
imgRobotHover = pygame.image.load('img/icons8-r2-d2-256-hover.png').convert_alpha()
imgRobotFaded = pygame.image.load('img/icons8-r2-d2-256-faded.png').convert_alpha()

imgRobotv2 = pygame.image.load('img/icons8-bmo-256.png').convert_alpha()
imgRobotv2Hover = pygame.image.load('img/icons8-bmo-256-hover.png').convert_alpha()
imgBip = pygame.image.load('img/icons8-bit.png').convert_alpha()
imgBipFaded = pygame.image.load('img/icons8-bit-faded.png').convert_alpha()

imgAlphaBeta = pygame.image.load('img/alphabeta.png').convert_alpha()
imgAlphaBetaHover = pygame.image.load('img/alphabeta-hover.png').convert_alpha()

imgMinMax = pygame.image.load('img/minmax.png').convert_alpha()
imgMinMaxHover = pygame.image.load('img/minmax-hover.png').convert_alpha()

imgYes = pygame.image.load('img/yes.png').convert_alpha()
imgYesHover = pygame.image.load('img/yesHover.png').convert_alpha()

imgNo = pygame.image.load('img/no.png').convert_alpha()
imgNoHover = pygame.image.load('img/noHover.png').convert_alpha()

imgGameBoard = pygame.image.load('img/tictactoe_board.png').convert_alpha()
imgGameCircle = pygame.image.load('img/tictactoe_circle.png').convert_alpha()
imgGameCross = pygame.image.load('img/tictactoe_cross.png').convert_alpha()

""" Button Setup
Button Setup with images and position/rect
# The Rect object represents a rectangle which is used to detect mouse events (like hovering or clicking)
"""
btHuman = pygame.Rect(250, 250, imgHuman.get_width(), imgHumanHover.get_height())
btRobot = pygame.Rect(789, 250, imgRobot.get_width(), imgRobotHover.get_height())
mainButtons = [btHuman, btRobot]

btalphabeta = pygame.Rect(250, 250, imgAlphaBeta.get_width(), imgAlphaBetaHover.get_height())
btminmax = pygame.Rect(789, 250, imgMinMax.get_width(), imgMinMaxHover.get_height())
algorithmButtons = [btalphabeta, btminmax]

btYes = pygame.Rect(260, 370, imgYes.get_width(), imgYesHover.get_height())
btNo = pygame.Rect(900, 370, imgNo.get_width(), imgNoHover.get_height())
confirmButtons = [btYes, btNo]

""" Button Images Setup 
These lists pair each button normal image with its hover image
"""
mainButtonImages = [
    (imgHuman, imgHumanHover),
    (imgRobot, imgRobotHover)
]

algorithmButtonImages = [
    (imgAlphaBeta, imgAlphaBetaHover),
    (imgMinMax, imgMinMaxHover)
]

confirmButtonImages = [
    (imgYes, imgYesHover),
    (imgNo, imgNoHover)
]

robotv2Images = [
    (imgRobotv2, imgRobotv2Hover)
]

""" Resize images for game screen """
imageSize = (125,125)
imgHumanGame = pygame.transform.scale(imgHuman, imageSize)
imgRobotGame = pygame.transform.scale(imgRobot, imageSize)
imgBipGame = pygame.transform.scale(imgBip, imageSize)
imgHumanFadedGame = pygame.transform.scale(imgHumanFaded, imageSize)
imgRobotFadedGame = pygame.transform.scale(imgRobotFaded, imageSize)
imgBipFadedGame = pygame.transform.scale(imgBipFaded, imageSize)