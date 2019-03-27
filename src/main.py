import pygame
from font import *
from gameUI import *
from connect4 import *

#Constants
WIN_WIDTH = 800
WIN_HEIGHT = 600
DEFAULT_COLOR = (224, 180, 20)
HOVER_COLOR = (247, 224, 140)
FONT = 'ressources/Birdy Game.ttf'

#Init window
pygame.init()
pygame.display.set_caption('Era Crew - Connect 4')
mainWindow = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
exitWindow = False
oldTicks = 0
delayInterval = 50
backgroundPicture = pygame.image.load("ressources/background.png").convert()
redCoin = pygame.image.load("ressources/redcoin.png").convert_alpha()
blueCoin = pygame.image.load("ressources/bluecoin.png").convert_alpha()
board = Board(mainWindow, backgroundPicture, DEFAULT_COLOR, FONT, redCoin, blueCoin)
pvpButton = Font(mainWindow, WIN_WIDTH/2, 50+WIN_HEIGHT/2, "Player vs Player", DEFAULT_COLOR, FONT, 45)
pveButton = Font(mainWindow, WIN_WIDTH/2, 150+WIN_HEIGHT/2, "Player vs AI", DEFAULT_COLOR, FONT, 45)
playagain = Font(mainWindow, WIN_WIDTH/2, WIN_HEIGHT/2 +100, "Play again", DEFAULT_COLOR, FONT, 40)

#Display
displayMenu(mainWindow, backgroundPicture, DEFAULT_COLOR, FONT)
pvpButton.draw()
pveButton.draw()

while not exitWindow:
    currentTicks = pygame.time.get_ticks()
    for event in pygame.event.get():
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            exitWindow = True
        if event.type == pygame.MOUSEMOTION:
            if not board.gamelaunched:
                pvpButton.hover(mousePos, HOVER_COLOR)
                pveButton.hover(mousePos, HOVER_COLOR)
            if board.gameover:
                playagain.hover(mousePos, HOVER_COLOR)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if board.gameover and playagain.isOver(mousePos):
                board.playAgain()
            if not board.gamelaunched and pvpButton.isOver(mousePos):
                board.startGame()
            elif not board.gamelaunched and pveButton.isOver(mousePos):
                board.startGame()
            elif board.gamelaunched:
                board.add_token(mousePos)
                if board.check_win2():
                    board.gameOver()
                    playagain.draw()
                    
    if currentTicks - oldTicks < delayInterval:
        pygame.time.delay(delayInterval - (currentTicks-oldTicks))
    pygame.display.flip()
    oldTicks = currentTicks