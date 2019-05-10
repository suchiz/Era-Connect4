import pygame
import math
from font import *

class GameUI():
    def __init__ (self, mainWindow, H, W, board):
        self.mainWindow = mainWindow
        self.board = board
        self.backgroundPicture = pygame.image.load("../ressources/background.png").convert()
        self.DEFAULT_COLOR = (224, 180, 20)
        self.HOVER_COLOR = (247, 224, 140)
        self.font = '../ressources/Birdy Game.ttf'
        self.redcoin = pygame.image.load("../ressources/redcoin.png").convert_alpha()
        self.bluecoin = pygame.image.load("../ressources/bluecoin.png").convert_alpha()
        self.BOARD_ROWS = 6
        self.BOARD_COLS = 7
        self.BOARD_WIDTH = 700
        self.BOARD_HEIGHT = 600
        self.WIN_WIDTH = W
        self.WIN_HEIGHT = H
        self.WIDTH_GAP = int((self.WIN_WIDTH-self.BOARD_WIDTH)/2)
        self.HEIGHT_GAP = int(self.WIN_HEIGHT-self.BOARD_HEIGHT)
        self.SQUARE_WIDTH = int(self.BOARD_WIDTH/self.BOARD_COLS)
        self.SQUARE_HEIGHT = int(self.BOARD_HEIGHT/self.BOARD_ROWS)
        self.pvpButton = Font(mainWindow, self.WIN_WIDTH/2, 50+self.WIN_HEIGHT/2, "Player vs Player", self.DEFAULT_COLOR, self.font, 45)
        self.pveButton = Font(mainWindow, self.WIN_WIDTH/2, 150+self.WIN_HEIGHT/2, "Player vs AI", self.DEFAULT_COLOR, self.font, 45)
        self.playagain = Font(mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2 +100, "Play again", self.DEFAULT_COLOR, self.font, 40)

    def displayGame(self):
        boardPicture = pygame.image.load("../ressources/Connect4Board.png").convert_alpha()
        self.mainWindow.blit(self.backgroundPicture, (0,0))
        self.mainWindow.blit(boardPicture, (self.WIDTH_GAP, self.HEIGHT_GAP))

    def displayCoin(self, mousePos):
        (row, col, player) = self.board.add_token(mousePos, self.WIDTH_GAP, self.SQUARE_WIDTH)
        if (player == 1):
            self.mainWindow.blit(self.redcoin, (self.WIDTH_GAP+col*self.SQUARE_WIDTH+(self.SQUARE_WIDTH-72)/2, self.WIN_HEIGHT-(row+1)*self.SQUARE_HEIGHT+(self.SQUARE_HEIGHT-72)/2))
        else:
            self.mainWindow.blit(self.bluecoin, (self.WIDTH_GAP+col*self.SQUARE_WIDTH+(self.SQUARE_WIDTH-72)/2, self.WIN_HEIGHT-(row+1)*self.SQUARE_HEIGHT+(self.SQUARE_HEIGHT-72)/2))

    def displayWinner(self, player):
        self.mainWindow.blit(self.backgroundPicture, (0,0))
        winner = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2-150, "Player " + str(player) + " won the game !", self.DEFAULT_COLOR, self.font, 60)
        winner.draw()
        self.playagain.draw()

    def displayMenu(self):
        self.mainWindow.blit(self.backgroundPicture, (0,0))
        title = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2-150, "Era-Connect4", self.DEFAULT_COLOR, self.font, 80)
        title.draw()
        self.pvpButton.draw()
        self.pveButton.draw()

    def hoverMenu(self, mousePos):
        if not self.board.gamelaunched:
            self.pvpButton.hover(mousePos, self.HOVER_COLOR)
            self.pveButton.hover(mousePos, self.HOVER_COLOR)
        if self.board.gameover:
            self.playagain.hover(mousePos, self.HOVER_COLOR)
    
    def clickEventManagement(self, mousePos):
        if self.board.gameover and self.playagain.isOver(mousePos):
            self.board.playAgain()
            self.displayMenu()

        if not self.board.gamelaunched and self.pvpButton.isOver(mousePos):
            self.board.startGame()
            self.displayGame()

        elif not self.board.gamelaunched and self.pveButton.isOver(mousePos):
            self.board.startGame()
            self.displayGame()

        elif self.board.gamelaunched:
            self.displayCoin(mousePos)
            if self.board.check_win2():
                self.board.gameOver()
                self.displayWinner(int(self.board.check_win()))
