import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()
    FPS = 60

    radius = 15 #radius of our circle
    x = 0
    y = 0
    mode = "blue"
    points = []

    while True:
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        #pumping event Q
        for event in pygame.event.get():
            #determine if attempt window close
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                #determine if any letter keys were pressed
                if event.key == pygame.K_r:
                    mode = "red"
                if event.key == pygame.K_g:
                    mode = "green"
                if event.key == pygame.K_b:
                    mode = "blue"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 : #left button clicked
                    radius = min(200,radius+1)
                if event.button == 3: #right button clicked
                    radius = max(1,radius-1)
                if event.button == 2: #middle button
                    radius = 15 #reset
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]
        #end event Q
        screen.fill((0,0,0))

            #draw all points on scrren
        for i in range(0,len(points)-1,1):
            draw_line_between(screen,i,points[i],points[i+1],radius,mode)


        pygame.display.flip()
        clock.tick(FPS)

def draw_line_between(screen,index,start,end,width,color_mode):
    c1 = max(0,min(255,2*index - 256))
    c2 = max(0,min(255,2*index))

    if color_mode == "blue":
        color = (c1,c1,c2)
    if color_mode == "green":
        color = (c1,c2,c1)
    if color_mode == "red":
        color = (c2,c1,c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx),abs(dy))

    for i in xrange(iterations):
        progress = 1.0*(float(i)/iterations)
        aprogress = 1.0 - progress
        x = aprogress*start[0] + progress*end[0]
        y = aprogress*start[1] + progress*end[1]
        pygame.draw.circle(screen,color,(int(x),int(y)),width)


main()