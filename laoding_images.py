import pygame
import os

_image_library = {} #private central string to surface dict

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None: #not initialized yet
        standardized_path = path.replace("/",os.sep).replace("\\",os.sep)
        image = pygame.image.load(standardized_path)#laod image
        _image_library[path] = image
    return image

#begin pygame script
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
clock = pygame.time.Clock()
FPS = 60

pygame.mixer.music.load("beep1.ogg")
pygame.mixer.music.play(0)
pygame.mixer.music.queue("beep1.ogg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255,255,255))
    screen.blit(get_image("ball.png"),(20,20))
    pygame.display.flip()
    clock.tick(FPS)
