from Player import *
from Map import *

#makes map
map1=open("Maps/Map1.txt")
Map=Map(map1)

#makes player
player=Player(Map.playerStartLocation)

#main runloop
while True:
    #for getting the fps and making movement work with any framerate
    dt=clock.tick()
    #for closing the game safely
    for event in pygame.event.get():
        if event.type==pygame.QUIT:os._exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:os._exit(0)
            elif event.key==pygame.K_w:player.movementDirection.y=-1
            elif event.key==pygame.K_s:player.movementDirection.y=1
            elif event.key==pygame.K_a:player.movementDirection.x=-1
            elif event.key==pygame.K_d:player.movementDirection.x=1
            elif event.key==pygame.K_LEFT:player.rotationDirection=2
            elif event.key==pygame.K_RIGHT:player.rotationDirection=-2
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w and player.movementDirection.y<0:player.movementDirection.y=0
            elif event.key==pygame.K_s and player.movementDirection.y>0:player.movementDirection.y=0
            elif event.key==pygame.K_a and player.movementDirection.x<0:player.movementDirection.x=0
            elif event.key==pygame.K_d and player.movementDirection.x>0:player.movementDirection.x=0
            elif event.key==pygame.K_LEFT and player.rotationDirection>0:player.rotationDirection=0
            elif event.key==pygame.K_RIGHT and player.rotationDirection<0:player.rotationDirection=0

    #resets the screen
    screen.fill("white")    
    
    #draws the map
    Map.draw()

    #draws the player
    player.draw()
    #moves the player
    player.move(dt)
    
    #for showing fps
    pygame.display.set_caption("Wolfenstien Clone, FPS: "+str(round(clock.get_fps())))
    
    #updates the screen
    pygame.display.update()
