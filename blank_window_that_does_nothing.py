import pygame

pygame.init() #get stuff initialized
screen = pygame.display.set_mode((400,300)) #lauch window, returns surface object
done = False

while not done: #while done is still false
    for event in pygame.event.get(): #this examines each action and clears the Q
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()