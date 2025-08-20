#imports
from Utils import *

#pixel color dither
def PixelColorDither(screen,image,x,y,xmove,ymove,threshold):
    if avgPixelGet(image,x,y)>threshold:screen.set_at((x+xmove,y+ymove),"white")
    else:screen.set_at((x+xmove,y+ymove),"black")
        
#Two By Two Ordered Dithering Function
def TwoByTwoOrderedDithering(screen,image,imageSize):
    #does the dithering for each 2X2 group of pixels
    for y in range(0,imageSize[1],2):
        for x in range(0,imageSize[0],2):
            #for top left pixel
            PixelColorDither(screen,image,x,y,0,0,191)
            #for top right pixel
            if x+1<imageSize[0]:PixelColorDither(screen,image,x,y,1,0,56)
            #for bottom left pixel
            if y+1<imageSize[1]:PixelColorDither(screen,image,x,y,0,1,112)
            #for bottom right pixel
            if x+1<imageSize[0] and y+1<imageSize[1]:PixelColorDither(screen,image,x,y,1,1,127)
        pygame.display.update()
    print("Two By Two Ordered Dithering Done")
    #saves image
    pygame.image.save(screen,"DitheredImages/TwoByTwoOrderedDithering.png")


#Two By Two Ordered Dithering Function
def ThreeByThreeOrderedDithering(screen,image,imageSize):
    #does the dithering for each 2X2 group of pixels
    for y in range(0,imageSize[1],3):
        for x in range(0,imageSize[0],3):
            #for top left pixel
            PixelColorDither(screen,image,x,y,0,0,229)
            #for top middle pixel
            if x+1<imageSize[0]:PixelColorDither(screen,image,x,y,1,0,102)
            #for top right
            if x+2<imageSize[0]:PixelColorDither(screen,image,x,y,2,0,153)
            #for middle left pixel
            if y+1<imageSize[1]:PixelColorDither(screen,image,x,y,0,1,76)
            #for middle pixel
            if y+1<imageSize[1] and x+1<imageSize[0]:PixelColorDither(screen,image,x,y,1,1,127)
            #for middle right pixel
            if y+1<imageSize[1] and x+2<imageSize[0]:PixelColorDither(screen,image,x,y,2,1,25)
            #for bottom left pixel
            if y+2<imageSize[1]:PixelColorDither(screen,image,x,y,0,2,178)
            #for bottom middle pixel
            if y+2<imageSize[1] and x+1<imageSize[0]:PixelColorDither(screen,image,x,y,1,2,51)
            #for bottom right pixel
            if y+2<imageSize[1] and x+2<imageSize[0]:PixelColorDither(screen,image,x,y,2,2,204)
        pygame.display.update()
    print("Three By Three Ordered Dithering Done")
    #saves image
    pygame.image.save(screen,"DitheredImages/ThreeByThreeOrderedDithering.png")
