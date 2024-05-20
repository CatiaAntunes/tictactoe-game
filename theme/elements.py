import pygame
# pygame must be initialized to use its functionalities
pygame.init()

""" Font setup
None = No default font is being used
normal = size 36
title = size 72
description = size 20
"""
normal = pygame.font.Font(None, 36)
title = pygame.font.Font(None, 72)
description = pygame.font.Font(None, 20)

""" Color setup """
white = pygame.Color('white')
salmon = pygame.Color('salmon')
darkred = pygame.Color('darkred')

""" Create Confirmation Labels and Position
Since we are making a label with variables, a function has been made to get those variables
We get the information by having adversary and algorithm as parameters in the main.py, inside the draw_confirmation_page(), where those variables are, and them importing everything from elements into drawPages.py where draw_confirmation_page() is defined. This way we don't have import issues.
"""
def get_confirmOptionLb(adversary, algorithm):
    text = f"So, you want BIP to play against some {adversary}\nwith the famous {algorithm} technique?!\nAre you sure?"
    return normal.render(text, True, white)
def get_confirmOptionLb_rect(lb):
    return lb.get_rect(center=(630, 250))

# Labels and their respective position configuration (rect)
titleLb = title.render("Tic Tac Toe", True, white)
titleLbRect = titleLb.get_rect(center=(640, 100))

titleDescLb = description.render("aka Jogo do Galo", True, darkred)
titleDescLbRect = titleDescLb.get_rect(center=(710, 120))

userOptionLb = normal.render("choose an option", True, white)
userOptionLbRect = userOptionLb.get_rect(center=(645, 360))
userOptionDescLb = description.render("you can't win btw", True, darkred)
userOptionDescLbRect = userOptionDescLb.get_rect(center=(645, 385))

algoOptionLb = normal.render("pick your poison", True, white)
algoOptionLbRect = algoOptionLb.get_rect(center=(645, 360))
algoOptionDescLb = description.render("we mean algorithm", True, darkred)
algoOptionDescLbRect = userOptionDescLb.get_rect(center=(645, 385))

bipLb = description.render("this is BIP, in case you're wondering", True, darkred)
bipLbRect = bipLb.get_rect(center=(640, 600))

