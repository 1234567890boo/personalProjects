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
            elif event.key==pygame.K_w:yGridMove=-1
            elif event.key==pygame.K_s:yGridMove=1
            elif event.key==pygame.K_a:xGridMove=-1
            elif event.key==pygame.K_d:xGridMove=1
            elif event.key==pygame.K_LEFT:gridRotationMovement=1
            elif event.key==pygame.K_RIGHT:gridRotationMovement=-1
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w and yGridMove!=1:yGridMove=0
            elif event.key==pygame.K_s and yGridMove!=-1:yGridMove=0
            elif event.key==pygame.K_a and xGridMove!=1:xGridMove=0
            elif event.key==pygame.K_d and xGridMove!=-1:xGridMove=0
            elif event.key==pygame.K_LEFT and gridRotation!=1:gridRotationMovement=0
            elif event.key==pygame.K_RIGHT and gridRotation!=-1:gridRotationMovement=0
            
    #resets the screen
    screen.fill("black")

    #moves and rotates the grid
    gridRotation+=gridRotationMovement
    rotatedTwoDSurf,rotatedTwoDSurfCenterX,rotatedTwoDSurfCenterY=gridDraw(grid,xGridMove,yGridMove,gridRotation)
    #do player things below here
    
    #draws the grid
    screen.blit(rotatedTwoDSurf,(rotatedTwoDSurfCenterX,rotatedTwoDSurfCenterY))
    
    #updates the screen
    pygame.display.update()
