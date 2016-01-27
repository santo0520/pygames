import pygame

pygame.init() #get stuff initialized
screen = pygame.display.set_mode((400,300)) #lauch window, returns surface object
done = False
is_blue = True

while not done: #while done is still false
    for event in pygame.event.get(): #this examines each action and clears the Q
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue #flip between blue and red
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    if is_blue:
        color = (0,0,255)
    else:
        color = (255,0,0)
    pygame.draw.rect(screen,color,pygame.Rect(100,30,120,60))
    pygame.display.flip()
