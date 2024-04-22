#import
import pygame,os
#inits pygame
pygame.init()
#variables
x,y=1004,576
direction="none"
files=next(os.walk("Layers"))#gets all files in layers folder
files=int(len(files[2]))#gets number of files
#makes background
bg=pygame.Surface((x,y))
bg.fill((50,50,50))
#sets screen size and name
screen=pygame.display.set_mode((x,y),pygame.SCALED,vsync=True)
pygame.display.set_caption("ParilaxBGTest")
#class for sprite for the paralax effect
class BackgroundBlock(pygame.sprite.DirtySprite):
    #init function
    def __init__(self,img,xpos,layer):
        super().__init__()
        self.layer=layer
        self.image=pygame.image.load(img).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=xpos
    #draw and movement function
    def update(self):
        if direction=="right":self.rect.move_ip(self.layer,0)
        elif direction=="left":self.rect.move_ip(-self.layer,0)
        if self.rect.x>x or self.rect.x<-x:self.rect.x=-self.rect.x
        self.dirty=1
#make sprites and adds to sprite list
sprites=[]
for i in range(0,files,1):
    for n in range (0,2,1):
        sprite=BackgroundBlock("Layers/layer"+str(i+1)+".png",n*x,i+1)
        sprites.append(sprite)
allSprites=pygame.sprite.LayeredDirty((sprites))
#main Runloop
while True:
    #clears screen
    allSprites.clear(screen,bg)
    #gets keypresses and button click for closing gameand moving the backgound
    for event in pygame.event.get():
        if event.type==pygame.QUIT:os._exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:direction="left"
            elif event.key==pygame.K_RIGHT:direction="right"
            elif event.key==pygame.K_ESCAPE:os._exit(0)
        elif event.type==pygame.KEYUP:direction="none"
        
    rects=allSprites.draw(screen)
    for sprite in allSprites:sprite.update()
    #updates the screen
    pygame.display.update(rects)

