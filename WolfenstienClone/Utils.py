#imports
import pygame,os
#initializes pygame
pygame.init()
#makes screen
x,y=500,500
flags=pygame.SCALED#|pygame.FULLSCREEN
screen=pygame.display.set_mode((x,y),flags,vsync=True)

#surface to draw the grid on
TwoDSurf=pygame.Surface((500,500)).convert_alpha()

#grid variables
xGridMove,yGridMove=0,0
rectGridList=[]

#grid for the 2D part
grid=[["W","W","W","W","W","W","W","W","W","W"],
      ["W","N","N","N","N","N","N","W","N","W"],
      ["W","N","N","N","N","N","N","W","N","W"],
      ["W","N","W","W","N","N","N","N","N","W"],
      ["W","N","W","W","N","N","N","N","N","W"],
      ["W","N","N","N","N","W","W","W","N","W"],
      ["W","N","N","N","N","W","N","W","N","W"],
      ["W","N","N","N","N","W","N","N","N","W"],
      ["W","N","N","N","N","W","N","N","N","W"],
      ["W","W","W","W","W","W","W","W","W","W"],]


#fills rectGidList with th rects for the future
for yGrid in range(0,len(grid),1):
    for xGrid in range(0,len(grid[yGrid]),1):
        if grid[yGrid][xGrid]=="W":rectGridList.append(pygame.Rect((xGrid*50,yGrid*50,50,50)))
