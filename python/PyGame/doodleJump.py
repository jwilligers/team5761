import pygame
import sys
import random
import colours


def setup():
    pygame.init()

    displayWidth = 600
    displayHeight = 1000
    displaySize = (displayWidth, displayHeight)
    FPS = 30

    speed = 1


    window = pygame.display.set_mode(displaySize)
    pygame.display.set_caption('Doodle Jump')


    score = 0


def platform(type, x, y):
    pygame.draw.rect()


def drawCharacter(window, x):
    pygame.draw.rect(window, colours.black, x, 900, 50, 50)

def gameLoop():
    gameExit = False
    gameOver = False
    x = 500
    while not gameExit:

        while gameOver == True:

            gameDisplay.fill(colours.white)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x -= 10
                    if event.key == pygame.K_RIGHT:
                        x += 10


            platform(normal, x, 200)
            pygame.display.update()

    pygame.display.update()

setup()
gameLoop()