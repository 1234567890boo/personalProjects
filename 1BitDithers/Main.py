#imports
from ThresholdDithering import *
from RandomDithering import *
from OrderedDithering import *

#imports image
image=pygame.image.load("image.png")
#gets the size of the image
imageSize=image.get_size()

#makes sscreen size equal to the image size
screen=pygame.display.set_mode((imageSize[0],imageSize[1]))

#threshold Dither is not a true dither, but a good start
ThresholdDithering(screen,image,imageSize)

#Clamped Random Dithering
ClampedRandomDithering(screen,image,imageSize)

#True Random Dithering
TrueRandomDithering(screen,image,imageSize)

#Two by Two Ordered Dithering
TwoByTwoOrderedDithering(screen,image,imageSize)

#Three by Three
ThreeByThreeOrderedDithering(screen,image,imageSize)

#closes window after it is done
os._exit(0)

    
