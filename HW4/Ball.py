#File Name:  Ball.py
#Purpose:    This will be used to draw a circle at its current location
#Author:     Khoa Nguyen
#id:         14295146
#Date:       02/16/2022
from Drawable import Drawable
import pygame

class Ball(Drawable):
    def __init__(self, x=0, y=0, size=1, color=(0, 0, 0), visibility=True):
        super().__init__(x, y, visibility)
        self.__size = size
        self.__color = color

    def get_rect(self):
        coordinate = self.getLoc()
        size = self.getSize()
        left = coordinate[0] - size
        top = coordinate[1] - size
        return pygame.Rect(left, top , size*2, size*2)

    def draw(self, surface):
        coordinate = self.getLoc()
        size = self.getSize()
        left = coordinate[0] + size

        if self.getVisible():
            pygame.draw.circle(surface, self.__color, (left, coordinate[1]), self.__size, 0)


    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getSize(self):
        return self.__size

    def setSize(self, s):
        self.__size = s
