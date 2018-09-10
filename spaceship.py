
import pygame
pygame.init()

black = [0,0,0]
white = [255,255,255]
# Set the height and width of the screen
screen_size = (900,700)
screen = pygame.display.set_mode(screen_size)
 
pygame.display.set_caption("Flying Warrior!")
background_image=pygame.image.load("images/background.jpg").convert()
ship_image = pygame.image.load("images/player_ship.png").convert()
ship_size = (50,37)
ship_image.set_colorkey(white)
 
done = False
clock = pygame.time.Clock()
 
while not done:
	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop
	
	mouse_position = pygame.mouse.get_pos()
	screen.blit(background_image, [0,0])
	screen.blit(ship_image, (mouse_position[0] - ship_size[0]//2,mouse_position[1] - ship_size[1]//2))
	
	pygame.display.flip()
	clock.tick(60)
 
pygame.quit()
