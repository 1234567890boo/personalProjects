from Utils import *
from Grid import *
#runloop
while True:
    #for closing the game safely
    for event in pygame.event.get():
        if event.type==pygame.QUIT:os._exit(0)
        #player movement and exiting when escape is pressed
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:os._exit(0)
            elif event.key==pygame.K_w:yGridMove-=1
            elif event.key==pygame.K_s:yGridMove=1
            elif event.key==pygame.K_a:xGridMove-=1
            elif event.key==pygame.K_d:xGridMove=1
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w:yGridMove=0
            elif event.key==pygame.K_s:yGridMove=0
            elif event.key==pygame.K_a:xGridMove=0
            elif event.key==pygame.K_d:xGridMove=0
            
    #resets the screen
    screen.fill("bisque4")

    #draws the grid
    TwoDSurfDraw(grid,xGridMove,yGridMove)
    
    #updates the screen
    pygame.display.update()
