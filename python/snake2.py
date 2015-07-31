import pygame

pygame.init()

red = (255, 0, 0)
white = (255, 255, 255)



display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
def gameloop():
	gameDisplay.fill(white)


	pygame.draw.rect(gameDisplay, red, [100, 100, 100, 100])
	pygame.display.update()
	
while 1:
	gameloop()