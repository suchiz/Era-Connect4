import numpy as np
import sys
from gameUI import *

class Board():
    def __init__ (self):
        self.ROWS = 6
        self.COLS = 7
        self.board = np.zeros((self.ROWS, self.COLS))
        self.turn = 1
        self.gamelaunched = False
        self.gameover = False

    def isValid(self, r, c):
        if (r >= 0 and r < self.ROWS and c >= 0 and c < self.COLS and self.board[r, c] == 0):
            return True
        return False

    def add_token(self, mousePos, WIDTH_GAP, SQUARE_WIDTH):
        posx = mousePos[0]
        col = math.floor((posx-WIDTH_GAP)/SQUARE_WIDTH)
        if self.turn%2 == 1:
            player = 1
        else:
            player = 2
        for row in range(self.ROWS):
            if self.board[row, col] == 0:
                break
        if self.isValid(row, col):
            self.board[row, col] = player      
            self.turn = self.turn + 1
        return(row, col, player)
        

    def check_win(self):
        # check horizontal line
        for r in range(self.ROWS):
            for c in range(self.COLS - 3):
                if self.board[r][c] != 0 and self.board[r][c+1] == self.board[r][c] and self.board[r][c+2] == self.board[r][c] and self.board[r][c+3] == self.board[r][c]:
                    return self.board[r][c]
        # check vertical line
        for c in range(self.COLS):
            for r in range(self.ROWS - 3):
                if self.board[r][c] != 0 and self.board[r+1][c] == self.board[r][c] and self.board[r+2][c] == self.board[r][c] \
                        and self.board[r+3][c] == self.board[r][c]:
                    return self.board[r][c]
        # check diagonal win from bottom left to up right
        for c in range(self.COLS - 3):
            for r in range(3, self.ROWS):
                if self.board[r][c] != 0 and self.board[r - 1][c + 1] == self.board[r][c] and self.board[r - 2][c + 2] == self.board[r][c] and \
                        self.board[r - 3][c + 3] == self.board[r][c]:
                    return self.board[r][c]
        # check diagonal win from up left to bottom right
        for c in range(self.COLS - 3):
            for r in range(self.ROWS - 3):
                if self.board[r][c] != 0 and self.board[r + 1][c + 1] == self.board[r][c] and self.board[r + 2][c + 2] == self.board[r][c] and \
                        self.board[r + 3][c + 3] == self.board[r][c]:
                    return self.board[r][c]
        return 0

    def check_win2(self):
        if (self.check_win() != 0):
            return True
        return False

    def gameOver(self):
        self.gameover = True

    def startGame(self):
        self.board = np.zeros((6, 7))
        self.turn = 1
        self.gamelaunched = True
    
    def playAgain(self):
        self.gamelaunched = False
        self.gameover = False
