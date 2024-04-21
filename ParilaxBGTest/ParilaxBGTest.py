#import
import pygame,os
#inits pygame
pygame.init()
#variables
x,y=1014,576
direction="none"
files=next(os.walk("Layers"))#gets all files in layers folder
files=int(len(files[2]))#gets number of files
#sets screen size and name
screen=pygame.display.set_mode((x,y),flags=pygame.SCALED,vsync=True)
pygame.display.set_caption("ParilaxBGTest")
#class for sprite for the paralax effect
class BackgroundBlock(pygame.sprite.Sprite):
    #init function
    def __init__(self,img,xpos,layer):
        super().__init__()
        self.layer=layer
        self.image=pygame.image.load(img).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=xpos
    #draw and movement function
    def draw(self):
        screen.blit(self.image,self.rect)
        if direction=="right":sprite.rect.x+=self.layer
        elif direction=="left":sprite.rect.x-=self.layer
        if self.rect.x>x or self.rect.x<-x:self.rect.x=-self.rect.x
#makes layers, layer 1 "closest" layer
layerList=[]
for l in range(0,files,1):
    layerName="layer"+str(l+1)
    layerName=pygame.sprite.Group()
    layerList.append(layerName)
#adds sprites to layers based on name
for e in range(len(layerList),0,-1):
    for i in range(0,2,1):
        layerSprite=BackgroundBlock("Layers/layer"+str(-e+len(layerList)+1)+".png",x*i,e)
        layerSprite.add(layerList[e-1])
#main Runloop
while True:
    #clears screen
    screen.fill((50,50,50))
    #gets keypresses and button click for closing gameand moving the backgound
    for event in pygame.event.get():
        if event.type==pygame.QUIT:os._exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:direction="left"
            elif event.key==pygame.K_RIGHT:direction="right"
        elif event.type==pygame.KEYUP:direction="none"
    #renders the layers
    for layer in layerList:
        for sprite in layer:sprite.draw()
    #updates the screen
    pygame.display.update()
