#imports
from Utils import *

#playes class
class Player:
    #initialises the class
    def __init__(self,startingPos,mapRectList):
        self.mapRectList=mapRectList
        self.startingPos=startingPos+pygame.Vector2(3,3)
        self.rect=pygame.FRect((self.startingPos.x,self.startingPos.y,14,14))
        self.movementDirection=pygame.Vector2(0,0)
        self.rotationDirection=0
        self.rotationDegrees=0
    #draws the player
    def draw(self):
        pygame.draw.rect(screen,"black",self.rect)
    #moves the player
    def moveCollide(self,dt):
        #for setting the movement speed for each direction to 1 or -1 for normalizing
        #for side to side direction
        if self.movementDirection.x>0:self.movementDirection.x=math.ceil(self.movementDirection.x)
        else:self.movementDirection.x=math.floor(self.movementDirection.x)
        #for up and down direction        
        if self.movementDirection.y>0:self.movementDirection.y=math.ceil(self.movementDirection.y)
        else:self.movementDirection.y=math.floor(self.movementDirection.y)
        #actually normalizes it
        if self.movementDirection.x!=0 and self.movementDirection.y!=0:self.movementDirection=self.movementDirection.normalize()
        #for moving in the direction that the player is looking
        self.rotationDegrees+=self.rotationDirection
        #applies the movement direction, actually moving the player
        movementVectorX=(self.movementDirection.x*dt)/10
        movementVectorY=(self.movementDirection.y*dt)/10
        movementVector=pygame.Vector2(movementVectorX,movementVectorY).rotate(-self.rotationDegrees)
        #does collisions and movement for the x direction
        self.rect.x+=movementVector.x
        allCollision=self.rect.collidelistall(self.mapRectList)
        for collision in allCollision:
            collidedRect=self.mapRectList[collision]
            if movementVector.x>0:self.rect.right=collidedRect.left
            elif movementVector.x<0:self.rect.left=collidedRect.right
        #does collisions and movement for the y direction
        self.rect.y+=movementVector.y
        allCollision=self.rect.collidelistall(self.mapRectList)
        for collision in allCollision:
            collidedRect=self.mapRectList[collision]
            if movementVector.y>0:self.rect.bottom=collidedRect.top
            elif movementVector.y<0:self.rect.top=collidedRect.bottom
