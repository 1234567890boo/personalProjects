#imports
from Utils import *

#Threshold dithering
def ThresholdDithering(screen,image,imageSize):
    #gets average color of the whole image
    threshold=avgImgGet(image,imageSize)
    #does the dithering per pixel
    for y in range(0,imageSize[1],1):
        for x in range(0,imageSize[0],1):
            #sues the avrg color as the threshold
            if image.get_at((x,y))[0]>threshold:screen.set_at((x,y),"white")
            else:screen.set_at((x,y),"black")
        pygame.display.update()
    print("Threshold Dithering Done")

    #saves image
    pygame.image.save(screen,"DitheredImages/ThresholdDitheredImage.png")
