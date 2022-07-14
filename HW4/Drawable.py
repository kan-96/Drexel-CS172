#File Name:  Drawable.py
#Purpose:    This will be used to make graphic applications
#Author:     Khoa Nguyen
#Date:       02/16/2022
import pygame
import abc

class Drawable(metaclass=abc.ABCMeta):
  def __init__(self, x=0, y=0, visibility=True):
    self.__x = x
    self.__y = y
    self.__visible = visibility

  def getLoc(self):
    return self.__x, self.__y

  def setLoc(self, p):
    self.__x = p[0]
    self.__y = p[1]

  def setVisible(self, visibility):
    self.__visible = visibility

  def getVisible(self):
    return self.__visible

  @abc.abstractmethod
  def get_rect(self):
    pass

  @abc.abstractmethod
  def draw(self, surface):
    pass
