import pygame
import math
from font import *

BOARD_ROWS = 6
BOARD_COLS = 7
BOARD_WIDTH = 700
BOARD_HEIGHT = 600
WIN_WIDTH = 800
WIN_HEIGHT = 600
WIDTH_GAP = int((WIN_WIDTH-BOARD_WIDTH)/2)
HEIGHT_GAP = int(WIN_HEIGHT-BOARD_HEIGHT)
SQUARE_WIDTH = int(BOARD_WIDTH/BOARD_COLS)
SQUARE_HEIGHT = int(BOARD_HEIGHT/BOARD_ROWS)

def displayGame(mainWindow, backgroundPicture):
    boardPicture = pygame.image.load("ressources/Connect4Board.png").convert_alpha()
    mainWindow.blit(backgroundPicture, (0,0))
    mainWindow.blit(boardPicture, (WIDTH_GAP, HEIGHT_GAP))

def displayCoin(mainWindow, coin, col, row):
    mainWindow.blit(coin, (WIDTH_GAP+col*SQUARE_WIDTH+(SQUARE_WIDTH-72)/2, WIN_HEIGHT-(row+1)*SQUARE_HEIGHT+(SQUARE_HEIGHT-72)/2))

def displayWinner(mainWindow, backgroundPicture, player, color, font):
    mainWindow.blit(backgroundPicture, (0,0))
    winner = Font(mainWindow, WIN_WIDTH/2, WIN_HEIGHT/2-150, "Player " + str(player) + " won the game !", color, font, 60)
    winner.draw()

def displayMenu(mainWindow, backgroundPicture, color, font):
    mainWindow.blit(backgroundPicture, (0,0))
    title = Font(mainWindow, WIN_WIDTH/2, WIN_HEIGHT/2-150, "Era-Connect4", color, font, 80)
    title.draw()

def getWidthGap():
    return WIDTH_GAP

def getSquareWidth():
    return SQUARE_WIDTH
