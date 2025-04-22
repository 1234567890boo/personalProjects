import pygame,os,math,functools,random

#gets size for the screen
screenX,screenY=640,480
#makes the screen and gives it a name
screen=pygame.display.set_mode((screenX,screenY),pygame.SCALED|pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE,vsync=True)
pygame.display.set_caption("Sprite Stacking")
#gets clock for fps
clock=pygame.time.Clock()
#for saving the maximum fps
maxFPS=0
minFPS=999999

#function for rendiering text
def renderText(text,color,x,y):
    font=pygame.font.Font(pygame.font.get_default_font(),30)
    word=font.render(text,1,color)
    screen.blit(word,(x,y))
