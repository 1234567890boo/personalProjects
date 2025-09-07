from Utils import *

#function to draw the grid onto the 2D surface
def gridDraw(grid,xMove,yMove,gridRotation):
    TwoDSurf.fill("bisque4")
    for rect in rectGridList:
        #for movement
        rect.x+=xMove
        rect.y+=yMove
        #makes the surface
        pygame.draw.rect(TwoDSurf,"white",rect)
    #rotates it
    rotatedTwoDSurf=pygame.transform.rotate(TwoDSurf,gridRotation)
    rotatedTwoDSurfRect=rotatedTwoDSurf.get_rect()
    rotatedTwoDSurfCenterX,rotatedTwoDSurfCenterY=rotatedTwoDSurfRect.center
    rotatedTwoDSurfCenterX-=rotatedTwoDSurfRect.width-(screenX/2)
    rotatedTwoDSurfCenterY-=rotatedTwoDSurfRect.height-(screenY/2)
    return rotatedTwoDSurf,rotatedTwoDSurfCenterX,rotatedTwoDSurfCenterY
