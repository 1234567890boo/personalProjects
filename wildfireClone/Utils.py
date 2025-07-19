#imports
import pygame,os

#starts pygame
pygame.init()

#makes screen variables
screenX,screenY=1280,720

#makes screen
screen=pygame.display.set_mode((screenX,screenY),pygame.SCALED|pygame.RESIZABLE|pygame.SRCALPHA,vsync=True)
