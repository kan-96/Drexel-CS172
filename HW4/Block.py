#File Name:  Block.py
#Purpose:    This will be used to draw a square with a black outline at its current location
#Author:     Khoa Nguyen
#id:         14295146
#Date:       02/16/2022
from Drawable import Drawable
import pygame

class Block(Drawable):
    def __init__(self, x=0, y=0, size=1, color=(0, 0, 0), visibility=True):
        super().__init__(x, y, visibility)
        self.__size = size
        self.__color = color

    def get_rect(self):
        size = self.getSize()
        position = self.getLoc()
        return pygame.Rect(position[0],position[1], size,size)

    def draw(self, surface):
        outline_color = (0, 0, 0)
        outline_w = 2
        if self.getVisible():
            #draw filled block
            pygame.draw.rect(surface, self.__color, self.get_rect(), 0)
            #draw outline
            pygame.draw.rect(surface, outline_color,self.get_rect(),outline_w)

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getSize(self):
        return self.__size

    def setSize(self, s):
        self.__size = s

