#imports
import pygame,os,math

#initializes pygame
pygame.init()

#makes screen
screenX,screenY=320,200
flags=pygame.SCALED#|pygame.FULLSCREEN
screen=pygame.display.set_mode((screenX,screenY),flags,vsync=True)


#gets clock for fps
clock=pygame.time.Clock()

#function for rendering text
def renderText(text,color,x,y):
    font=pygame.font.Font(pygame.font.get_default_font(),15)
    word=font.render(text,False,color)
    screen.blit(word,(x,y))

    

