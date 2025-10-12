#imports
from Utils import *

#makes player
class Player:
    #ran when player is made
    def __init__(self,startLocation,mapRectList):
        self.mapRectList=mapRectList
        self.pos=startLocation
        self.width=15
        self.height=15
        self.surface=pygame.Surface((self.width,self.height))
        self.rect=self.surface.get_rect(center=self.pos)
        self.xMovementDirection="None"
        self.yMovementDirection="None"
        self.rotationDegrees=0
        self.rotationDirection="None"
        self.rayHalfWidth=100
        self.rayDistance=325
        self.visionEndPoints=[]
        self.distanceEndPoints=[]
    #draws the player
    def draw(self):
        screen.blit(self.surface,self.rect)
        for point in self.visionEndPoints:pygame.draw.line(screen,"red",point,self.pos)
    def moveLook(self):
        self.visionEndPoints=[]
        self.distanceEndPoints=[]
        movement=pygame.Vector2(0,0)
        #does the collisions
        if self.xMovementDirection=="Left":movement.x-=1
        elif self.xMovementDirection=="Right":movement.x+=1
        if self.yMovementDirection=="Forward":movement.y-=1
        elif self.yMovementDirection=="Backward":movement.y+=1
        if movement.x!=0 and movement.y!=0:movement=movement.normalize()
        #does the collision
        collision=self.rect.collidelist(self.mapRectList)
        if collision>0:
            rightCollision=abs(self.mapRectList[collision].left-self.rect.right)
            leftCollision=abs(self.mapRectList[collision].right-self.rect.left)
            topCollision=abs(self.mapRectList[collision].bottom-self.rect.top)
            bottomCollision=abs(self.mapRectList[collision].top-self.rect.bottom)

            if rightCollision<leftCollision and rightCollision<bottomCollision and rightCollision<topCollision:self.pos.x-=rightCollision
            elif leftCollision<rightCollision and leftCollision<bottomCollision and leftCollision<topCollision:self.pos.x+=leftCollision
            elif bottomCollision<rightCollision and bottomCollision<topCollision and bottomCollision<leftCollision:self.pos.y-=bottomCollision
            elif topCollision<rightCollision and topCollision<bottomCollision and topCollision<leftCollision:self.pos.y+=topCollision

        #actually moves the player
        self.pos+=movement
        self.rect.center=self.pos
        #rays for 3D goes here, for loop sets the number of rays
        if self.rotationDirection=="Left":self.rotationDegrees+=1
        elif self.rotationDirection=="Right":self.rotationDegrees-=1
        #for drawing the end points
        endLineStart=pygame.Vector2(self.pos.x,self.pos.y)-(pygame.Vector2(-self.rayHalfWidth,self.rayDistance).rotate(-self.rotationDegrees))
        endLineEnd=pygame.Vector2(self.pos.x,self.pos.y)-(pygame.Vector2(self.rayHalfWidth,self.rayDistance).rotate(-self.rotationDegrees))
        for point in range(0,screenX,1):self.visionEndPoints.append(endLineStart.lerp(endLineEnd,point/screenX))
        #for drawing the points for distance calculation
        distanceLineStart=pygame.Vector2(self.pos.x,self.pos.y)-(pygame.Vector2(-self.rayHalfWidth,0).rotate(-self.rotationDegrees))
        distanceLineEnd=pygame.Vector2(self.pos.x,self.pos.y)-(pygame.Vector2(self.rayHalfWidth,0).rotate(-self.rotationDegrees))
        for point in range(0,screenX,1):self.distanceEndPoints.append(distanceLineStart.lerp(distanceLineEnd,point/screenX))





