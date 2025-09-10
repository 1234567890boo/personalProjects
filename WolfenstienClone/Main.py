from Utils import *
from Grid import *
#makes an instance of the map
map=Grid(startingGrid)
#runloop
while True:
    #for closing the game safely
    for event in pygame.event.get():
        if event.type==pygame.QUIT:os._exit(0)
        #player movement and exiting when escape is pressed
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:os._exit(0)
            elif event.key==pygame.K_w:map.yMovement="Forward"
            elif event.key==pygame.K_s:map.yMovement="Backward"
            elif event.key==pygame.K_a:map.xMovement="Left"
            elif event.key==pygame.K_d:map.xMovement="Right"
            if event.key==pygame.K_LEFT:map.rotationDirection="Left"
            elif event.key==pygame.K_RIGHT:map.rotationDirection="Right"
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_w and map.yMovement!="Backward":map.yMovement="None"
            elif event.key==pygame.K_s and map.yMovement!="Forward":map.yMovement="None"
            elif event.key==pygame.K_a and map.xMovement!="Right":map.xMovement="None"
            elif event.key==pygame.K_d and map.xMovement!="Left":map.xMovement="None"
            if event.key==pygame.K_LEFT and map.rotationDirection!="Right":map.rotationDirection="None"
            elif event.key==pygame.K_RIGHT and map.rotationDirection!="Left":map.rotationDirection="None"
            
    #resets the screen
    screen.fill("black")

    #draws the map
    map.drawMove()

    #updates the screen
    pygame.display.update()
