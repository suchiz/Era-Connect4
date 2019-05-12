import pygame
import math
from font import *
from network import *

class GameUI():
    def __init__ (self, mainWindow, H, W, board):
        self.mainWindow = mainWindow
        self.board = board
        self.network = Network(self)
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
        self.backButton = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2 +100, "Back to Menu", self.DEFAULT_COLOR, self.font, 40)
        self.mediumButton = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2, "Pussy mode", self.DEFAULT_COLOR, self.font, 40)
        self.difficultButton = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2 +60, "Ok mode", self.DEFAULT_COLOR, self.font, 40)
        self.impossibleButton = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2 +150, "YOU GOT GUTS MODE", self.DEFAULT_COLOR, self.font, 60)


    def displayGame(self):
        boardPicture = pygame.image.load("../ressources/Connect4Board.png").convert_alpha()
        self.mainWindow.blit(self.backgroundPicture, (0,0))
        self.mainWindow.blit(boardPicture, (self.WIDTH_GAP, self.HEIGHT_GAP))

    def displayCoin2(self, col):
        (row, col, player) = self.board.add_token2(col)
        if player == 1:
            self.mainWindow.blit(self.redcoin, (self.WIDTH_GAP+col*self.SQUARE_WIDTH+(self.SQUARE_WIDTH-72)/2, self.WIN_HEIGHT-(row+1)*self.SQUARE_HEIGHT+(self.SQUARE_HEIGHT-72)/2))
        elif player == 2:
            self.mainWindow.blit(self.bluecoin, (self.WIDTH_GAP+col*self.SQUARE_WIDTH+(self.SQUARE_WIDTH-72)/2, self.WIN_HEIGHT-(row+1)*self.SQUARE_HEIGHT+(self.SQUARE_HEIGHT-72)/2))

    def displayCoin(self, mousePos):
        (row, col, player) = self.board.add_token(mousePos, self.WIDTH_GAP, self.SQUARE_WIDTH)
        if player == 1:
            self.mainWindow.blit(self.redcoin, (self.WIDTH_GAP+col*self.SQUARE_WIDTH+(self.SQUARE_WIDTH-72)/2, self.WIN_HEIGHT-(row+1)*self.SQUARE_HEIGHT+(self.SQUARE_HEIGHT-72)/2))
        elif player == 2:
            self.mainWindow.blit(self.bluecoin, (self.WIDTH_GAP+col*self.SQUARE_WIDTH+(self.SQUARE_WIDTH-72)/2, self.WIN_HEIGHT-(row+1)*self.SQUARE_HEIGHT+(self.SQUARE_HEIGHT-72)/2))

    def displayWinner(self, player):
        self.mainWindow.blit(self.backgroundPicture, (0,0))
        winner = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2-150, "Player " + str(player) + " won the game !", self.DEFAULT_COLOR, self.font, 60)
        winner.draw()
        self.backButton.draw()

    def displayMenu(self):
        self.mainWindow.blit(self.backgroundPicture, (0,0))
        title = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2-150, "Era-Connect4", self.DEFAULT_COLOR, self.font, 80)
        title.draw()
        self.pvpButton.draw()
        self.pveButton.draw()
    
    def displayDifficulty(self):
        self.mainWindow.blit(self.backgroundPicture, (0,0))
        title = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2-150, "Era-Connect4", self.DEFAULT_COLOR, self.font, 80)
        title.draw()
        self.mediumButton.draw()
        self.difficultButton.draw()
        self.impossibleButton.draw()

    

    def hoverMenu(self, mousePos):
        if not self.board.gamelaunched and not self.network.error and not self.network.waitplayer and not self.board.AIgame:
            self.pvpButton.hover(mousePos, self.HOVER_COLOR)
            self.pveButton.hover(mousePos, self.HOVER_COLOR)
        elif self.board.gameover:
            self.backButton.hover(mousePos, self.HOVER_COLOR)
        elif self.network.error:
            self.backButton.hover(mousePos, self.HOVER_COLOR)
        elif self.board.AIgame and not self.board.gamelaunched:
            self.mediumButton.hover(mousePos, self.HOVER_COLOR)
            self.difficultButton.hover(mousePos, self.HOVER_COLOR)
            self.impossibleButton.hover(mousePos, self.HOVER_COLOR)
    
    def clickEventManagement(self, mousePos):
        if self.board.gameover and self.backButton.isOver(mousePos):
            self.board.playAgain()
            self.displayMenu()

        if not self.board.gamelaunched and not self.board.AIgame and self.pvpButton.isOver(mousePos) and not self.network.error and not self.network.waitplayer:
            self.board.AIgame = False
            self.network = Network(self)
            if self.network.connect():
                self.network.listen()
    
        elif not self.board.gamelaunched and not self.board.AIgame and self.pveButton.isOver(mousePos) and not self.network.error and not self.network.waitplayer:
            self.board.AIgame = True
            self.displayDifficulty()

        elif not self.board.gamelaunched and self.board.AIgame and self.mediumButton.isOver(mousePos):
            self.board.difficulty = 0
            self.board.startGame()
            self.displayGame()
        elif not self.board.gamelaunched and self.board.AIgame and self.difficultButton.isOver(mousePos):
            self.board.difficulty = 1
            self.board.startGame()
            self.displayGame()
        elif not self.board.gamelaunched and self.board.AIgame and self.impossibleButton.isOver(mousePos):
            self.board.difficulty = 2
            self.board.startGame()
            self.displayGame()
        elif not self.board.gamelaunched and self.network.error and self.backButton.isOver(mousePos):
            self.network.error = False
            self.displayMenu()

        elif self.board.gamelaunched:
            if self.board.turn % 2 == 1 and self.board.AIgame:
                self.displayCoin(mousePos)
                if self.board.check_win2():
                    self.board.gameOver()
                    self.displayWinner(int(self.board.check_win()))
            else:
                if (self.board.turn % 2 == self.board.player):
                    self.playCoin_ToNetwork(mousePos)

############################## NETWORKING PART

    def displayErrorMessage(self, msg):
        errormsg = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2-150, msg, self.DEFAULT_COLOR, self.font, 50)
        self.mainWindow.blit(self.backgroundPicture, (0,0))
        errormsg.draw()
        self.backButton.draw()

    def displayWaitPlayer(self):
        self.mainWindow.blit(self.backgroundPicture, (0,0))
        waitplayer = Font(self.mainWindow, self.WIN_WIDTH/2, self.WIN_HEIGHT/2-150, "Waiting for players ...", self.DEFAULT_COLOR, self.font, 50)
        waitplayer.draw()

    def startGame_FromNetwork(self, player):
        self.board.player = player
        self.board.startGame()
        self.displayGame()

    def playCoin_ToNetwork(self, mousePos):
        (row, col, player) = self.board.computeCoinDatas(mousePos, self.WIDTH_GAP, self.SQUARE_WIDTH)
        if player == 0:
            return
        message = "playcoin-" + str(row) + "-" + str(col) + "-" + str(player)
        try:
            self.network.send(message)
        except socket.error:
            self.network.disconnect()

    def playCoin_FromNetwork(self, row, col, player):
        self.board.add_token_FromNetWork(int(row), int(col), int(player))
        if self.board.check_win2():
                self.board.gameOver()
                self.displayWinner(int(self.board.check_win()))
                self.network.disconnect()
        else:
            if (int(player) == 1):
                self.mainWindow.blit(self.redcoin, (self.WIDTH_GAP+int(col)*self.SQUARE_WIDTH+(self.SQUARE_WIDTH-72)/2, self.WIN_HEIGHT-(int(row)+1)*self.SQUARE_HEIGHT+(self.SQUARE_HEIGHT-72)/2))
            else:
                self.mainWindow.blit(self.bluecoin, (self.WIDTH_GAP+int(col)*self.SQUARE_WIDTH+(self.SQUARE_WIDTH-72)/2, self.WIN_HEIGHT-(int(row)+1)*self.SQUARE_HEIGHT+(self.SQUARE_HEIGHT-72)/2))

