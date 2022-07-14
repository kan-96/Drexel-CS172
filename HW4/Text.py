#File Name:  Text.py
#Purpose:    Text class, this will be used to diplay the player's score
#Author:     Khoa Nguyen
#id:         14295146
#Date:       02/16/2022
from Drawable import Drawable
import pygame

class Text(Drawable):
    def __init__(self, x=0, y=0, message = '', visibility=True):
        super().__init__(x, y, visibility)
        self.__message = message
        fontObj = pygame.font.Font("freesansbold.ttf", 32)
        self.__surface = fontObj.render(message, True, (0,0,0))

    def get_rect(self):
        position = self.getLoc
        size = fontObj.size(self.__message)
        return pygame.Rect(position[0], position[1], size[0], size[1])

    def draw(self, surface):
        if self.getVisible():
            surface.blit(self.__surface, self.getLoc())

    def getMess(self):
        return self.__message

    def setMess(self, mess):
        self.__message = mess
        fontObj = pygame.font.Font("freesansbold.ttf", 32)
        self.__surface = fontObj.render(mess, True, (0,0,0))

