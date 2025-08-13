#imports
from Utils import *

#general Random Dither Fucntion 
def generalRandomDither(screen,image,imageSize,thresholdMin,thresholdmax):
    #does the dithering for each pixel
    for y in range(0,imageSize[1],1):
        for x in range(0,imageSize[0],1):
            #randomly generates the threshold per pixel
            threshold=random.randint(thresholdMin,thresholdmax)
            #gets the average of a pixel
            avg=avgPixelGet(image,x,y)
            #does the dithering
            if avg>threshold:screen.set_at((x,y),"white")
            else:screen.set_at((x,y),"black")
        #updates the screen
        pygame.display.update()

#Clamped Random Dithering
def ClampedRandomDithering(screen,image,imageSize):
    #gets average color of the whole image
    threshold=avgImgGet(image,imageSize)
    #the higher the number the less white
    thresholdMin=threshold-60
    #the higher the number the more black
    thresholdmax=threshold+45
    generalRandomDither(screen,image,imageSize,thresholdMin,thresholdmax)
    print("Clamped Random Dithering Done")
    #saves image
    pygame.image.save(screen,"DitheredImages/ClampedRandomDitheredImage.png")


#True Random Dither
def TrueRandomDithering(screen,image,imageSize):
    #gets average color of the whole image
    generalRandomDither(screen,image,imageSize,0,255)
    print("True Random Dithering Done")
    #saves image
    pygame.image.save(screen,"DitheredImages/TrueRandomDitheredImage.png")
