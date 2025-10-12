from Player import *
from Map import *

map1=open("Maps/Map1.txt")
Map=Map(map1)

player=Player(Map.playerStartLocation,Map.mapListRect)

#main runloop
while True:
    #for closing the game safely
    for event in pygame.event.get():
        if event.type==pygame.QUIT:os._exit(0)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:os._exit(0)
            elif event.key==pygame.K_w:player.yMovementDirection="Forward"
            elif event.key==pygame.K_s:player.yMovementDirection="Backward"
            elif event.key==pygame.K_a:player.xMovementDirection="Left"
            elif event.key==pygame.K_d:player.xMovementDirection="Right"
            elif event.key==pygame.K_LEFT:player.rotationDirection="Left"
            elif event.key==pygame.K_RIGHT:player.rotationDirection="Right"
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w and player.yMovementDirection!="Backward":player.yMovementDirection=None
            elif event.key==pygame.K_s and player.yMovementDirection!="Forward":player.yMovementDirection=None
            elif event.key==pygame.K_a and player.xMovementDirection!="Right":player.xMovementDirection=None
            elif event.key==pygame.K_d and player.xMovementDirection!="Left":player.xMovementDirection=None
            elif event.key==pygame.K_LEFT and player.rotationDirection!="Right":player.rotationDirection=None
            elif event.key==pygame.K_RIGHT and player.rotationDirection!="Left":player.rotationDirection=None

    #resets the screen
    screen.fill("white")

    #draws the map
    Map.draw()
    
    #draws the player
    player.moveLook()
    player.draw()

    #for calculation and showing fps
    clock.tick()
    fps=clock.get_fps()
    if fps>maxFPS:maxFPS=fps
    if fps<minFPS and fps!=0:minFPS=fps
    displayedText="FPS: "+str(int(fps))+",  Min: "+str(int(maxFPS))+",  Max: "+str(int(minFPS))
    renderText(displayedText,"black",10,10)
    
    #updates the screen
    pygame.display.update()
