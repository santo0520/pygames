#a small program that writes hello world
import pygame


_cached_fonts = {}
_cached_text = {} #caches rendered text surface

def make_font(fonts,size):
    #get list of all available fonts in system
    available = pygame.font.get_fonts()
    choices = map(lambda x:x.lower().replace(' ',''),fonts)#strip space
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice,size)
    #default
    return pygame.font.Font(None,size)

def get_font(font_preferences,size):
    """get font from caches, if not load into cache"""
    global _cached_fonts
    key = str(font_preferences)+"|"+str(size)
    font = _cached_fonts.get(key,None)
    if font == None:
        font = make_font(font_preferences,size)#make new
        _cached_fonts[key] = font
    return font

def create_text(text,fonts,size,color):
    global _cached_text
    key = "|".join(map(str,(fonts,size,color,text)))
    image = _cached_text.get(key,None)
    if image == None:
        font = get_font(fonts,size)
        image = font.render(text,True,color)
        _cached_text[key] = image
    return image

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
done = False

font_preferences = [
        "Bizarre-Ass Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]
#text we want
text = create_text("hello, world1!",font_preferences,144,(255,0,0))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255,255,255))#paint screen white
    screen.blit(text,((640-text.get_width())//2,(480-text.get_height())//2))
    pygame.display.flip()
    clock.tick(60)