import pygame

pygame.init() #get stuff initialized
screen = pygame.display.set_mode((400,300)) #lauch window, returns surface object
done = False
is_blue = True
x = 30
y = 30
FPS = 60
clock = pygame.time.Clock()

while not done: #while done is still false
    for event in pygame.event.get(): #this examines each action and clears the Q
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    pressed_keys = pygame.key.get_pressed() #returns list of 0,1s indicating which keys are pressed

    if pressed_keys[pygame.K_UP]:
        y -= 3
    if pressed_keys[pygame.K_DOWN]:
        y+=3
    if pressed_keys[pygame.K_RIGHT]:
        x+=3
    if pressed_keys[pygame.K_LEFT]:
        x-= 3

    if is_blue:
        color = (0,0,255)
    else:
        color = (255,0,0)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,color,pygame.Rect(x,y,60,60))
    pygame.display.flip()
    #will blobk execution until 1/60 seconds has passed since last tick was called
    clock.tick(60)
