import pygame

pygame.init()

normal = pygame.font.Font(None, 36)
title = pygame.font.Font(None, 72)
description = pygame.font.Font(None, 20)

# Colors
white = pygame.Color('white')
salmon = pygame.Color('salmon')
darkred = pygame.Color('darkred')

# Labels
titleLb = title.render("Tic Tac Toe", True, white)
titleLb_rect = titleLb.get_rect(center=(640, 100))

titleDescLb = description.render("aka Jogo do Galo", True, darkred)
titleDescLb_rect = titleDescLb.get_rect(center=(710, 120))

userOptionLb = normal.render("choose an option", True, white)
userOptionLb_rect = userOptionLb.get_rect(center=(645, 360))
userOptionDescLb = description.render("you can't win btw", True, darkred)
userOptionDescLb_rect = userOptionDescLb.get_rect(center=(645, 385))

algoOptionLb = normal.render("pick the poison", True, white)
algoOptionLb_rect = algoOptionLb.get_rect(center=(645, 360))