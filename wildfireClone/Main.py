#imports
from Player import *

#makes player
player=Player("Sprites/Test.png")

#main runloop
while True:
    
    #for closing the window
    for event in pygame.event.get():
        if event.type==pygame.QUIT:os._exit(0)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:os._exit(0)
            
    #resets the screen every frame
    screen.fill("azure4")

    #draws the player
    player.draw()
    
    #updates screen
    pygame.display.update()
