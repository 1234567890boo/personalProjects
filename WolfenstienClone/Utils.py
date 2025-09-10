#imports
import pygame,os,math
#initializes pygame
pygame.init()
#makes screen
screenX,screenY=500,500
flags=pygame.SCALED#|pygame.FULLSCREEN
screen=pygame.display.set_mode((screenX,screenY),flags,vsync=True)



#grid for the 2D part
startingGrid=[]
grid=[["N","N","N","N","N","N","N","N","N","N"],
      ["N","N","N","N","N","N","N","N","N","N"],
      ["N","N","N","N","N","N","N","N","N","N"],
      ["N","N","N","N","N","N","N","N","N","N"],
      ["N","N","N","N","N","N","N","N","N","N"],
      ["N","N","N","N","N","N","N","N","N","N"],
      ["N","N","N","N","N","N","N","N","N","N"],
      ["N","N","N","N","N","N","N","W","N","N"],
      ["N","N","N","N","N","N","N","N","N","N"],
      ["N","N","N","N","N","N","N","N","N","N"],]


#fills rectGidList with the rects for the future, does this on app startup
for yGrid in range(0,len(grid),1):
    for xGrid in range(0,len(grid[yGrid]),1):
        if grid[yGrid][xGrid]=="W":
            startingGrid.append(pygame.Rect((xGrid*50,yGrid*50,50,50)))

