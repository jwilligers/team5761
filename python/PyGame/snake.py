import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)


display_width = 1000
display_height = 700
blockSize = 15
FPS = 30

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')


font = pygame.font.SysFont(None, 25)

pygame.display.flip()

def snake(blockSize, snakeList):
    for segment in snakeList:
        pygame.draw.rect(gameDisplay, green, [segment[0], segment[1], blockSize, blockSize])

def message_to_screen(msg,colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def gameLoop():

    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-blockSize)/blockSize)*blockSize
    randAppleY = round(random.randrange(0, display_height-blockSize)/blockSize)*blockSize

    clock = pygame.time.Clock()

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over. Final Score = " + str(snakeLength), red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit game")
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -blockSize
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = blockSize
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -blockSize
                if event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = blockSize

        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change


        gameDisplay.fill(white)
        AppleThickness = 20
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True


        snake(blockSize, snakeList)
        pygame.display.update()

        if(lead_x > randAppleX and lead_x < randAppleX+AppleThickness) or (lead_x + blockSize > randAppleX and lead_x + blockSize < randAppleX+AppleThickness):
            if(lead_y > randAppleY and lead_y < randAppleY+AppleThickness) or (lead_y + blockSize > randAppleY and lead_y + blockSize < randAppleY+AppleThickness):
                randAppleX = round(random.randrange(0, display_width - blockSize) / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - blockSize) / 10.0) * 10.0
                snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()