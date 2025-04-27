#imports
from SpriteStackingClass import *
#starts pygame
pygame.init()


#uses class to make object
blueCar=spriteStack("Sprites/BlueCar.png",screenX//2,screenY//2,16,16,0,1,0)

#stress test Make
cars=[]

for n in range(0,200,1):
    red=spriteStack("YellowCar.png",random.randint(0,screenX),random.randint(0,screenY),16,16,random.randint(0,360),1,0)
    cars.append(red)


#main runloop
while True:
    #resets screen for next frame
    screen.fill("darkgray")
    #draws the spritestack
    blueCar.draw()
    blueCar.rotoMove()
    
    #Stress test Start
    for car in cars:
        spriteChoice=random.choice(["BlueCar.png","RedCar.png","YellowCar.png","PurpleCar.png","GreenCar.png"])
        car.spriteSheet=pygame.image.load("Sprites/"+spriteChoice).convert_alpha()
        car.movementSpeed=random.random()
        car.draw()
        car.rotoMove()
    #Stress Test End
    
    #shows fps on screen
    dt=clock.tick()
    fps=clock.get_fps()
    if fps>maxFPS:maxFPS=fps
    if fps<minFPS and fps!=0:minFPS=fps
    displayedText="FPS: "+str(int(fps))+" maxFPS: "+str(int(maxFPS))+" minFPS: "+str(int(minFPS))
    renderText(displayedText,"red",10,10)
    
    #for closing the game safely
    for event in pygame.event.get():
        if event.type==pygame.QUIT:os._exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:os._exit(0)
        #for going left and right
            if event.key==pygame.K_w:blueCar.movementSpeed=1
            if event.key==pygame.K_a:blueCar.rotateBy=1
            if event.key==pygame.K_s:blueCar.movementSpeed=-1
            if event.key==pygame.K_d:blueCar.rotateBy=-1
        #so the sprite stack doesnt keep going once the key isnt pressed anymore
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w:blueCar.movementSpeed=0
            if event.key==pygame.K_a:blueCar.rotateBy=0
            if event.key==pygame.K_s:blueCar.movementSpeed=0
            if event.key==pygame.K_d:blueCar.rotateBy=0

    #updates screen
    pygame.display.update()



