import pygame, sys
 2. from pygame.locals import *
 3.
 4. pygame.init()
 5. DISPLAYSURF = pygame.display.set_mode((400, 300))
 6. pygame.display.set_caption('Hello World!')
 7. while True: # main game loop
 8.     for event in pygame.event.get():
 9.         if event.type == QUIT:
10.             pygame.quit()
11.             sys.exit()
12.     pygame.display.update()