#imports
from Utils import *

#makes map class
class Map:
    #initialises the map and makes a list that is better for rendering and collisions
    def __init__(self,startingMapList):
        self.playerStartLocation=pygame.Vector2(0,0)
        self.startingMapList=startingMapList.readlines()
        self.mapRectList=[]
        #adds the rect into the rect List
        for y in range(0,len(self.startingMapList),1):
            for x in range(0,len(self.startingMapList[y]),1):
                if self.startingMapList[y][x]=="W":self.mapRectList.append(pygame.Rect(x*20,y*20,20,20))
                elif self.startingMapList[y][x]=="P":self.playerStartLocation=pygame.Vector2(x*20,y*20)
    #draws the map
    def draw(self):
        for rect in self.mapRectList:pygame.draw.rect(screen,"blue",rect)
