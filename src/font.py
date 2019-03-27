import pygame 

class Font():
    def __init__(self, mainWindow, posx, posy, text, color, font, size):
        self.mainWindow = mainWindow
        self.posx = posx;
        self.posy = posy;
        self.text = text
        self.color = color;
        self.font = font;
        self.size = size;
        self.render = None

    def draw(self):
        font = pygame.font.Font(self.font, self.size)
        text = font.render(self.text, 1, self.color)
        self.render = text
        self.mainWindow.blit(text, (self.posx-self.render.get_width()/2, self.posy-self.render.get_height()/2))

    def draw2(self, color):
        font = pygame.font.Font(self.font, self.size)
        text = font.render(self.text, 1, color)
        self.render = text
        self.mainWindow.blit(text, (self.posx-self.render.get_width()/2, self.posy-self.render.get_height()/2))
    
    def isOver(self, mousePos):
        if mousePos[0] > self.posx-self.render.get_width()/2 and mousePos[0] < self.posx + self.render.get_width()/2:
            if mousePos[1] > self.posy-self.render.get_height()/2 and mousePos[1] < self.posy + self.render.get_height()/2:    
                return True
        return False

    def hover(self, mousePos, color):
        if(self.isOver (mousePos)):
            self.draw2(color)
        else:
            self.draw()