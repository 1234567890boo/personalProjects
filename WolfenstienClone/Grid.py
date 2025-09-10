#imports
from Utils import *

#makes class
class Grid:
    #initalizes all variabes
    def __init__(self,startingGrid):
        self.startingGrid=startingGrid
        self.map=pygame.Surface((500,500)).convert_alpha()
        self.rotationDegrees=0
        self.rotationDirection="None"
        self.offset=pygame.Vector2(0,0)
        self.xMovement="None"
        self.yMovement="None"
        self.rectSurface=pygame.Surface((self.startingGrid[0].width,self.startingGrid[0].height)).convert_alpha()
    #draws and moves the map
    def drawMove(self):
        #resets the map surface
        self.map.fill("bisque4")
        #movement names based off of what the player would see in 3D
        if self.xMovement=="Left":self.offset.x-=1
        elif self.xMovement=="Right":self.offset.x+=1
        if self.yMovement=="Forward":self.offset.y+=1
        elif self.yMovement=="Backward":self.offset.y-=1
        #for rotation
        if self.rotationDirection=="Left":self.rotationDegrees+=1
        elif self.rotationDirection=="Right":self.rotationDegrees-=1
        #for drawing
        for rect in self.startingGrid:
            self.rectSurface.fill("white")
            #rotation code goes here
            rotatedSurface=pygame.transform.rotate(self.rectSurface,self.rotationDegrees)
            origin=pygame.Vector2(rect.x,rect.y)
            pivot=pygame.Vector2(screenX/2,screenY/2)
            rotatedSurfaceOffset=pivot+(origin-pivot).rotate(-self.rotationDegrees)
            rotatedSurfaceRect=rotatedSurface.get_rect(center=rotatedSurfaceOffset)
            #acctually moves the rect
            rotatedSurfaceRect.x+=self.offset.x
            rotatedSurfaceRect.y+=self.offset.y
            rect=rotatedSurfaceRect
            #draws the rect onto the screen
            self.map.blit(rotatedSurface,rect)
        #drws the map onto the screen
        screen.blit(self.map,(0,0))
