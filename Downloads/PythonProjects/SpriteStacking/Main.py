#imports
import pygame,os,math
#starts pygame
pygame.init()
#gets size for the screen
screenX,screenY=640,480
#makes the screen and gives it a name
screen=pygame.display.set_mode((screenX,screenY),pygame.SCALED|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE,vsync=True)
pygame.display.set_caption("Sprite Stacking")


#sprite stacking class start

class spriteStack:
    #initializes all variables that will be used
    def __init__(self,spriteSheet,x,y,width,height,rotation,spriteSeparation,movementSpeed):
        self.surface=pygame.Surface((width,height),pygame.SRCALPHA|pygame.HWSURFACE)
        self.spriteSheet=pygame.image.load(spriteSheet).convert_alpha()
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.rotation=rotation
        self.spriteSeparation=spriteSeparation
        self.movementSpeed=movementSpeed
    #draw function
    def draw(self):
        for i in range (0,self.spriteSheet.get_width()//self.width,1):
            #puts the first sprte of the sprite sheet on the surface
            self.surface.fill((0,0,0,0))
            self.surface.blit(self.spriteSheet,(-i*self.width,0))
            #rotates the sprite
            rotatedSurface=pygame.transform.rotate(self.surface,self.rotation)
            #gets center of rotated sprite
            rotatedSurfaceCenterX=rotatedSurface.get_width()//2
            rotatedSurfaceCenterY=rotatedSurface.get_height()//2
            #draws surface on the screen
            screen.blit(rotatedSurface,(self.x-rotatedSurfaceCenterX,(self.y-(i*self.spriteSeparation))-rotatedSurfaceCenterY))
    #rotation and movement function
    def rotoMove(self,rotateBy):
        #changes the rotation of the sprite stack
        self.rotation+=rotateBy
        #gets the rotation in radians
        rotationInRadians=math.radians(self.rotation)
        #moves the spritestack
        self.x+=math.sin(rotationInRadians+(math.pi/2))*self.movementSpeed
        self.y+=math.cos(rotationInRadians+(math.pi/2))*self.movementSpeed

#spritestacking class end

blueCar=spriteStack("Sprites/BlueCar.png",screenX//2,screenY//2,16,16,0,1,1)

#main runloop
while True:
    #resets screen for next frame
    screen.fill("darkgray")
    #draws and moves the spritestack
    blueCar.draw()
    blueCar.rotoMove(1)
    #for closing the game safely
    for event in pygame.event.get():
        if event.type==pygame.QUIT:os._exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:os._exit(0)

    #updates screen
    pygame.display.update()



