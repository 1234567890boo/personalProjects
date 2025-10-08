#imports
import pygame,os,math

#initializes pygame
pygame.init()

#makes screen
screenX,screenY=320,200
flags=pygame.SCALED#|pygame.FULLSCREEN
screen=pygame.display.set_mode((screenX,screenY),flags,vsync=True)
