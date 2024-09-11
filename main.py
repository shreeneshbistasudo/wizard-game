import pygame
pygame.init()

#variables 
running=True
screen = pygame.display.set_mode((800,600))


player=pygame.image.load('Wizard Pack/Idle.png').convert_alpha()

def get_image(img,width,height):
	image=pygame.Surface((width,height)).convert_alpha()
	image.blit(img,(250,250),(0,0, width,height))
	return image


frame_0=get_image(player,175,145)

while running:
	screen.blit(frame_0,(250,250))

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
	pygame.display.update()

pygame.quit()
