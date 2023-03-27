import pygame
import time
current_time=time.localtime()
cuurent_minute=current_time.tm_min
current_second=current_time.tm_sec
pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("Micky Mouse Clock")
image=pygame.image.load('mickeyclock.jpeg')
resized_image = pygame.transform.scale(image, (400, 400))
done = False
#clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.blit(resized_image, (0,0))
    pygame.display.flip()
    #clock.tick(60)
