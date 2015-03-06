import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Hello World!')

while True:
	pygame.draw.rect(window, (255,0,0), (100, 100, 50, 50))
	pygame.draw.rect(window, (0,255,0), (150, 100, 50, 50))
	pygame.draw.rect(window, (0,0,255), (200, 100, 50, 50))
	
	pygame.display.update()