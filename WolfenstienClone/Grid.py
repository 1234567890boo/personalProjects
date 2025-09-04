from Utils import *

#function to draw the grid onto the 2D surface
def TwoDSurfDraw(grid,xMove,yMove):
    TwoDSurf.fill((0,0,0,0))
    for rect in rectGridList:
        rect.x+=xMove
        rect.y+=yMove
        pygame.draw.rect(TwoDSurf,"white",rect)
    #blits the 2d surface onto the screen
    screen.blit(TwoDSurf,(0,0))
