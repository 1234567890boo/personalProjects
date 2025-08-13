import pygame,os,random,time

#funtion for getting the avg color of a pixel
def avgPixelGet(image,x,y):
    #makes variables that are used
    avg=0
    pixel=image.get_at((x,y))
    #averages the pixel
    avg+=pixel[0]
    avg+=pixel[1]
    avg+=pixel[2]
    avg=avg//3
    return avg


def avgImgGet(image,imageSize):
    #variable for getting the average color
    avgR=0
    avgG=0
    avgB=0
    color=0
    #gets average color of the whole image per color channel
    for y in range(0,imageSize[1],1):
        for x in range(0,imageSize[0],1):
            pixel=image.get_at((x,y))
            avgR+=pixel[0]
            avgG+=pixel[1]
            avgB+=pixel[2]
    avgR=avgR/(imageSize[0]*imageSize[1])
    avgG=avgG/(imageSize[0]*imageSize[1])
    avgB=avgB/(imageSize[0]*imageSize[1])
    #averagesand returns the color channels
    return int((avgR+avgG+avgB)/3)-25
