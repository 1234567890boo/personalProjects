#imports
from Utils import *

#makes player
class Player:
    #ran when player is made
    def __init__(self):
        self.pos=pygame.Vector2(screenX/2,screenY/2)
        self.width=20
        self.height=20
        self.surface=pygame.Surface((self.width,self.height))
        self.rect=self.surface.get_rect(center=self.pos)
        self.xMovementDirection="None"
        self.yMovementDirection="None"
        self.rotationDegrees=0
        self.rotationDirection="None"
        self.rayHalfWidth=50
    #draws the player
    def draw(self):
        #moves the player
        movement=pygame.Vector2(0,0)
        if self.xMovementDirection=="Left":movement.x-=1
        elif self.xMovementDirection=="Right":movement.x+=1
        if self.yMovementDirection=="Forward":movement.y-=1
        elif self.yMovementDirection=="Backward":movement.y+=1
        if movement.x!=0 and movement.y!=0:movement=movement.normalize()
        self.pos+=movement
        self.rect.center=self.pos
        #draws the player
        screen.blit(self.surface,self.rect)
        #rays for 3D goes here, for loop sets the number of rays
        if self.rotationDirection=="Left":self.rotationDegrees+=1
        elif self.rotationDirection=="Right":self.rotationDegrees-=1
        #for drawing the end points
        pos1=pygame.Vector2(self.pos.x,self.pos.y)-(pygame.Vector2(-self.rayHalfWidth,100).rotate(-self.rotationDegrees))
        pos2=pygame.Vector2(self.pos.x,self.pos.y)-(pygame.Vector2(self.rayHalfWidth,100).rotate(-self.rotationDegrees))
        for point in range(0,screenX,1):
            pos=pos1.lerp(pos2,point/screenX)
            pygame.draw.line(screen,"red",pos,self.pos)






