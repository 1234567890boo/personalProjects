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


#map editor
#checks if the file itself ws ran by me or just called by the main file
if __name__ == "__main__":
    '''
    when placing blocks or presets, it will replace what is already placed
    legend formap editor:
    backspace - resets map to empty
    s - saves map with input of name with file extentions
    w - makes wall at the mouse position
    p - makes a player at the mouse position and deleted any other player
    n - deletes what is at the place of the mouse
    1 - preset that clears the screen and adds walls around the edges
    '''
    #empty map template
    editMap=[["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],
             ["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],
             ["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],
             ["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],
             ["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],
             ["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],
             ["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],
             ["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],
             ["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],
             ["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N"],]
    #will open a file if it is there, leaves file creation to when saving happens:
    print("Map file location?")
    if input().lower()=="editing":
        mapName=input()
        try:
            mapFile=open(mapName)
            mapLines=mapFile.readlines()
            for y in range(0,len(mapLines),1):
                for x in range(0,len(mapLines[y])-1,1):
                    editMap[y][x]=mapLines[y][x]
        except: pass
    #runloop
    while True:
        #for getting mouse pos for placing walls
        mousePos=pygame.mouse.get_pos()
        mousePos=pygame.Vector2(mousePos[0]//20,mousePos[1]//20)
        #for exiting
        for event in pygame.event.get():
            if event.type==pygame.QUIT:os._exit(0)
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:os._exit(0)
                #saves the map into a txt file with a name
                elif event.key==pygame.K_s:
                    print("File Name and Location?")
                    name=input()
                    file=open(name,"w")
                    for line in editMap:
                        lineToSave=""
                        for point in line:
                            lineToSave+=point
                        lineToSave+="\n"
                        file.write(lineToSave)
                    file.close()
                    print("Saved!")
                #resets the map
                elif event.key==pygame.K_BACKSPACE:
                    for y in range(0,len(editMap),1):
                        for x in range(0,len(editMap[y]),1):
                            editMap[y][x]="N"
                #for placing walls
                elif event.key==pygame.K_w:editMap[int(mousePos.y)][int(mousePos.x)]="W"
                #for placing player, making sure there is always only 1 player on the map
                elif event.key==pygame.K_p:
                    for y in range(0,len(editMap),1):
                        for x in range(0,len(editMap[y]),1):
                            if editMap[y][x]=="P":editMap[y][x]="N"
                    editMap[int(mousePos.y)][int(mousePos.x)]="P"
                #for removing a place
                elif event.key==pygame.K_n:editMap[int(mousePos.y)][int(mousePos.x)]="N"
                #presets
                #walls around the all of the sides:
                elif event.key==pygame.K_1:
                    editMap=[["W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W"],
                             ["W","N","N","N","N","N","N","N","N","N","N","N","N","N","N","W"],
                             ["W","N","N","N","N","N","N","N","N","N","N","N","N","N","N","W"],
                             ["W","N","N","N","N","N","N","N","N","N","N","N","N","N","N","W"],
                             ["W","N","N","N","N","N","N","N","N","N","N","N","N","N","N","W"],
                             ["W","N","N","N","N","N","N","N","N","N","N","N","N","N","N","W"],
                             ["W","N","N","N","N","N","N","N","N","N","N","N","N","N","N","W"],
                             ["W","N","N","N","N","N","N","N","N","N","N","N","N","N","N","W"],
                             ["W","N","N","N","N","N","N","N","N","N","N","N","N","N","N","W"],
                             ["W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W"],]
        #resets screen
        screen.fill("white")
        #draws the map
        for y in range(0,len(editMap),1):
            for x in range(0,len(editMap[y]),1):
                if editMap[y][x]=="W":pygame.draw.rect(screen,"blue",(x*20,y*20,20,20))
                if editMap[y][x]=="P":pygame.draw.rect(screen,"black",(3+x*20,3+y*20,14,14))
        #draws a border around the position in the map the mouse is over
        pygame.draw.rect(screen,"azure4",(mousePos.x*20,mousePos.y*20,20,20),2)
        #updates the screen
        pygame.display.update()

