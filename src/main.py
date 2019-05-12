import pygame
import random
from gameUI import *
from aiPlayer import *
from connect4 import *

#Constants
WIN_WIDTH = 800
WIN_HEIGHT = 600

HUMAN = 1
AI = 0

EASY = 0
NORMAL = 1
DIFFICULT = 2

#Init window
pygame.init()
pygame.display.set_caption('Era Crew - Connect 4')
mainWindow = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
exitWindow = False
oldTicks = 0
delayInterval = 50

board = Board()
gameUI = GameUI(mainWindow, WIN_HEIGHT, WIN_WIDTH, board)

gameUI.displayMenu()


while not exitWindow:
    currentTicks = pygame.time.get_ticks()

    for event in pygame.event.get():
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            gameUI.network.disconnect()
            exitWindow = True
        if event.type == pygame.MOUSEMOTION:
            gameUI.hoverMenu(mousePos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            gameUI.clickEventManagement(mousePos)

    if board.turn % 2 == AI and board.AIgame and not board.gameover:
        ai_move(board, gameUI)
                    
    if currentTicks - oldTicks < delayInterval:
        pygame.time.delay(delayInterval - (currentTicks-oldTicks))
    pygame.display.flip()
    oldTicks = currentTicks