#File Name:  main.py
#Purpose:    Main script, set up the scene and launching the ball
#Author:     Khoa Nguyen
#id:         14295146
#Date:       02/16/2022

from typing import Tuple

from Drawable import Drawable
from Ball import Ball
from Block import Block
from Text import Text
import pygame
import random

def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (
            rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
        return True
    return False

if __name__ == "__main__":
    # main scrip starts here
    # initialization
    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    width, height = 600, 600

    pygame.init()
    surface = pygame.display.set_mode((width, height))
    #caption of tab
    pygame.display.set_caption('Cs172-Hw4')
    # add back ground scene
    imgSurface = pygame.image.load('mario.jpg')

    fpsClock = pygame.time.Clock()

    # list of drawable objects to be displayed
    drawables = []
    # create ground plane
    groundPlane = 400
    # instance of the Ball class
    ballSize = 15
    x_ball = 0
    y_ball = groundPlane - ballSize
    xv = 0
    yv = 0
    ball = Ball(int(x_ball), int(y_ball), ballSize, red)
    # instance of Block class
    numBlock = 9
    blockSize = 30
    blocks = []
    for w in range(0, 3):
        for h in range(1, 4):
            blocks.append(Block(400 + w * blockSize, groundPlane - h * blockSize, blockSize, blue))

    # & display score
    score = 0
    score_str = 'Score: {}'
    score_display = Text(0, 5, score_str.format(score))
    high_score = 0
    hsc_str = 'High Score: {}'
    hsc_display = Text(350, 5, hsc_str.format(high_score))

# lauching the ball with the loop MouseButtonUp and MouseButtonDown
    drawables = []
    ballRunning = False
    endGame = False
    newGame = False
    dt = 0.1
    g = 6.67
    R = 0.7
    eta = 0.5

#game loop
    while True:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            # Store the respective mouse location


            if not endGame:
                # MOUSEBUTTONDOWN
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDown_pos = pygame.mouse.get_pos()

                # MOUSEBUTTONUP
                if event.type == pygame.MOUSEBUTTONUP:
                    mouseUp_pos = pygame.mouse.get_pos()
                    xv = mouseUp_pos[0] - mouseDown_pos[0]
                    yv = mouseUp_pos[1] - mouseDown_pos[1]
                    ballRunning = True
                    endGame = True
            if newGame:
                if event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_y:

                    #reset all data
                    score = 0
                    endGame = False
                    newGame = False
                    ballRunning = False
                    ball.setLoc((0,groundPlane-ballSize))
                    x_ball, y_ball = ball.getLoc()

                    #reset block
                    for block in blocks:
                        block.setVisible(True)

                elif (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_n):
                    pygame.quit()
                    exit()

        # reset surface
        surface.fill(white)
        #background image
        surface.blit(imgSurface, (0,0))
        # draw block
        for block in blocks:
            block.draw(surface)
        # draw a line
        ground_line = pygame.draw.line(surface, black, (0, groundPlane), (width, groundPlane), 3)
        # draw a ball
        ball.draw(surface)

        # when a ball is running
        if ballRunning:
            if abs(yv) > 0.0001:
                if y_ball > groundPlane-ballSize:
                    x_ball += dt * xv
                    yv = -R * yv
                    xv = eta * xv
                    y_ball = groundPlane-ballSize
                else:
                    yv = yv - dt * g
                    x_ball += dt * xv
                    y_ball -= dt * yv
            if yv < 0.0001 and xv < 0.0001:
                ballRunning = False
            if not (0 < x_ball < groundPlane) or not (0 < y_ball < groundPlane):
                ballRunning = False
            #update ball location
            ball.setLoc((int(x_ball), int(y_ball)))

        # Hitting block

        for block in blocks:
            hit = intersect(ball.get_rect(), block.get_rect())
            if hit:
                if block.getVisible():
                    score += 1
                    if score >= high_score:
                        high_score = score
                block.setVisible(False)
        #update score
        score_display.setMess(score_str.format(score))
        score_display.draw(surface)
        hsc_display.setMess(hsc_str.format(high_score))
        hsc_display.draw(surface)
        #new game
        if endGame and not ballRunning:
            new_game_str ="Press [y]: a new game or [n]: exit"
            new_game_display = Text(50,100,new_game_str)
            new_game_display.draw(surface)
            newGame = True
        pygame.display.update()
        fpsClock.tick(30)







