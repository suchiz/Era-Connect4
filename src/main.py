import pygame
import random
from gameUI import *
from connect4 import *

#Constants
WIN_WIDTH = 800
WIN_HEIGHT = 600
DEFAULT_COLOR = (224, 180, 20)
HOVER_COLOR = (247, 224, 140)
FONT = '../ressources/Birdy Game.ttf'

HUMAN = 1
AI = 0

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
            exitWindow = True
        if event.type == pygame.MOUSEMOTION:
            gameUI.hoverMenu(mousePos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            gameUI.clickEventManagement(mousePos)

    if board.turn % 2 == AI and board.AIgame is True and not board.gameover:
        col = random.randint(0, board.COLS-1)
        gameUI.displayCoin2(col)
        if board.check_win2():
            board.gameOver()
            gameUI.displayWinner(int(board.check_win()))
                    
    if currentTicks - oldTicks < delayInterval:
        pygame.time.delay(delayInterval - (currentTicks-oldTicks))
    pygame.display.flip()
    oldTicks = currentTicks