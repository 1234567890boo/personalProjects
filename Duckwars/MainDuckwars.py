#imports
import os
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import DirectDialog,DirectButton
from panda3d.bullet import *
#game class
class Game(ShowBase):
    #inits
    def __init__(self):
        #sets global variables
        global font,keymap,width,isPlay,wp
        #inits showbase
        ShowBase.__init__(self)
        #disables default camera controls
        self.disableMouse()
        #gets window properties
        wp=WindowProperties()
        #sets size
        width=base.pipe.getDisplayWidth()
        height=base.pipe.getDisplayHeight()
        wp.setSize(width,height)
        base.win.requestProperties(wp)
        #starts bullet physics engine and adds gravity
        #bulletWorld=BulletWorld()
        #bulletWorld.setGravity(Vec3(0, 0, -9.81))
        #makes font
        font=loader.loadFont('font.ttf')
        font.setPixelsPerUnit(100)
        font.setPageSize(512,512)
        #global variables
        keymap={"forward":False,"backward":False,"leftStrafe":False,"rightStrafe":False}
        isPlay=False
        #inits options screen
        Game.Options()
        Game.OptionsClose()
        #inits and opens menu screen
        Game.Menu()
    #when called, updated one keymap peramiter to True or False
    def UpdateKeyMap(keyName,keyControl):
        keymap[keyName]=keyControl
    #moves the camera, and is called every frame
    def PlayerMovement(task):
        #for camera movement
        if keymap["forward"]:player.setPos(player,0,1,0)
        if keymap["backward"]:player.setPos(player,0,-1,0)
        if keymap["leftStrafe"]:player.setPos(player,-0.5,0,0)
        if keymap["rightStrafe"]:player.setPos(player,0.5,0,0)
        #for mouse movement
        player.setH(player.getH()-int((base.win.getPointer(0).getX()-base.win.getXSize()/2)*0.5))
        base.camera.setP(base.camera.getP()-int((base.win.getPointer(0).getY()-base.win.getYSize()/2)*0.5))
        base.win.movePointer(0,int(base.win.getXSize()/2),int(base.win.getYSize()/2))
        #mouse movement capping
        if base.camera.getP()>87:base.camera.setP(87)
        if base.camera.getP()<-87:base.camera.setP(-87)
        #sets camera pos to player model
        base.camera.setPos(player,0,1,2.5)
        base.camera.setH(player,0)
        #stops task if the options screen is not hidden
        if optionsScreen.isHidden()==False:
            return task.done
        return task.cont
    #opens options screen
    def OptionsOpen():
        if optionsScreen.isHidden()==True:
            wp.setCursorHidden(False)
            base.win.requestProperties(wp)
            optionsScreen.cleanup()
            Game.Options()
    #closes option screen
    def OptionsClose():
        optionsScreen.hide()
        if taskMgr.hasTaskNamed("PlayerMovement")==False and isPlay==True:
            wp.setCursorHidden(True)
            base.win.requestProperties(wp)
            base.win.movePointer(0,int(base.win.getXSize()/2),int(base.win.getYSize()/2))
            taskMgr.add(Game.PlayerMovement,"PlayerMovement")
    #eventual loading screen for my game
    def Load(whatLoading):
        menuScreen.cleanup()
        optionsScreen.hide()
        if whatLoading=="Play":
            Game.Play()
    #menu screen
    def Menu():
        global menuScreen
        menuScreen=DirectDialog(frameSize=(0,0,0,0))
        nameText=OnscreenText(text="Duckwars:Beaks Of Rage",parent=menuScreen,scale=0.3,pos=(0,0.7),fg=(255,255,255,255),shadow=(0,0,0,255),font=font)
        playButton=DirectButton(text="Play",parent=menuScreen,scale=0.1,pos=(-1,0,0.3),frameSize=(-3,3,-0.4,0.9),command=Game.Load,extraArgs=["Play"])
        optionsButton=DirectButton(text="Options",parent=menuScreen,scale=0.1,pos=(-1,0,0.1),frameSize=(-3,3,-0.4,0.9),command=Game.OptionsOpen)
        quitButton=DirectButton(text="Quit",parent=menuScreen,scale=0.1,pos=(-1,0,-0.1),frameSize=(-3,3,-0.4,0.9),command=Game.Quit)
    #options screen
    def Options():
        global optionsScreen
        optionsScreen=DirectDialog(frameSize=(-1.2,1.2,-0.7,0.7),pos=(0,0,-0.1))
        optionsText=OnscreenText(text="Options",parent=optionsScreen,scale=0.2,pos=(0,0.5,0),font=font)
        doneButton=DirectButton(text="Done",parent=optionsScreen,scale=0.1,pos=(-0.2,0,-0.6),command=Game.OptionsClose)
        quitButton=DirectButton(text="Quit",parent=optionsScreen,scale=0.1,pos=(0.2,0,-0.6),command=Game.Quit)
    #where the main game loop will go
    def Play():
        global isPlay,player,bulletWorld
        isPlay=True
        wp.setCursorHidden(True)
        base.win.requestProperties(wp)
        #makes environment
        environment=loader.loadModel("Models/BoxingRing.glb")
        environment.reparentTo(render)
        #for player rendering and gravity
        player=loader.loadModel("Models/Player.glb")
        player.reparentTo(render)
        #starts the movement task in the task manager
        taskMgr.add(Game.PlayerMovement,"PlayerMovement")
        #detects keys and updates the keymap accordingly
        base.accept("escape",Game.OptionsOpen)
        base.accept("w",Game.UpdateKeyMap,["forward",True])
        base.accept("w-up",Game.UpdateKeyMap,["forward",False])
        base.accept("s",Game.UpdateKeyMap,["backward",True])
        base.accept("s-up",Game.UpdateKeyMap,["backward",False])
        base.accept("a",Game.UpdateKeyMap,["leftStrafe",True])
        base.accept("a-up",Game.UpdateKeyMap,["leftStrafe",False])
        base.accept("d",Game.UpdateKeyMap,["rightStrafe",True])
        base.accept("d-up",Game.UpdateKeyMap,["rightStrafe",False])
    #quits game
    def Quit():
        base.graphicsEngine.removeAllWindows()
        os._exit(0)
#runs game
game=Game()
game.run()
