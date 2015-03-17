import pygame

pygame.init()

gameWindowX = 1000
gameWindowY = 700

blockSize = 15

gameDisplay = pygame.display.set_mode((gameWindowX, gameWindowY))
pygame.display.set_caption('Snake')

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type = pygame.QUIT:
            gameExit = True

pygame.quit()
quit()