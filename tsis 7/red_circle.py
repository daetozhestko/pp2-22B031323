import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("SUPERHOT")
done = True
color=(255,0,0)
x=300
y=300
speed=20
clock=pygame.time.Clock()
while done:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>speed+20:
        y-=speed
    if pressed[pygame.K_DOWN]and y<500-speed-20:
        y+=speed
    if pressed[pygame.K_RIGHT] and x<500-speed-25:
        x+=speed
    if pressed[pygame.K_LEFT] and x>speed+25:
        x-=speed
    pygame.draw.circle(screen,color,(x,y),50)
    pygame.display.flip()
    clock.tick(30)
        
    