#imports
from Utils import *

#makes player class
class Player:

    #initializes class
    def __init__(self,spriteSheet):
        self.spriteSheet=pygame.image.load(spriteSheet).convert_alpha()
        self.spriteSheetWidth=self.spriteSheet.get_width()
        self.spriteSheetHeight=self.spriteSheet.get_height()
        self.surface=pygame.Surface((self.spriteSheetWidth,self.spriteSheetWidth),pygame.SRCALPHA)
        self.pos=pygame.Vector2((screenX//2),(screenY//2))
        self.rotation=0
        self.spriteSeparation=0.75
    #draws the player when called
    def draw(self):
        #
        for n in range(0,self.spriteSheetHeight//self.spriteSheetWidth,1):
            #resets Surface for next slice
            self.surface.fill((0,0,0,0))
            #draws the next slice onto the surface
            self.surface.blit(self.spriteSheet,(0,-self.spriteSheetHeight+(n*self.spriteSheetWidth)))
            #for rotating the surface
            rotatedSurface=pygame.transform.rotate(self.surface,self.rotation)
            rotatedSurfaceCenterX=rotatedSurface.get_width()//2
            rotatedSurfaceCenterY=rotatedSurface.get_height()//2
            #draws surface on the screen
            screen.blit(rotatedSurface,(self.pos.x-rotatedSurfaceCenterX,(self.pos.y-(n*self.spriteSeparation))-rotatedSurfaceCenterY))
        #for resenting the rotation
        if self.rotation==360:self.rotation=-1
