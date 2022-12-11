#imports
import sys
from direct.showbase.ShowBase import *
from direct.gui.OnscreenText import *
from direct.gui.DirectGui import *
from panda3d.core import *
#game class
class Game(ShowBase):
    #inits
    def __init__(self):
        #sets global variables
        global font,keymap,width,height
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
        #for testing
        wp.setSize(500,500)
        #for testing
        base.win.requestProperties(wp)
        #makes font
        font=loader.loadFont('font.ttf')
        font.setPixelsPerUnit(100)
        font.setPageSize(512,512)
        #global variables
        keymap={"forward":False,"backward":False,"leftStrafe":False,"rightStrafe":False}
        #inits options screen
        Game.Options()
        optionsScreen.hide()
        #inits and opens menu
        Game.Menu()
    #when called, updated one keymap peramiter to True or False
    def UpdateKeyMap(keyName,keyControl):
        keymap[keyName]=keyControl
    #moves the camera, and is called every frame
    def CameraMovement(task):
        #for camera movement
        if keymap["forward"]==True:
            base.camera.setPos(base.camera,0,1,0)
        if keymap["backward"]==True:
            base.camera.setPos(base.camera,0,-1,0)
        if keymap["leftStrafe"]==True:
            base.camera.setPos(base.camera,-0.5,0,0)
        if keymap["rightStrafe"]==True:
            base.camera.setPos(base.camera,0.5,0,0)
        #for mouse movement
        base.camera.setH(base.camera.getH()-int((base.win.getPointer(0).getX()-base.win.getXSize()/2)*0.5))
        base.camera.setP(base.camera.getP()-int((base.win.getPointer(0).getY()-base.win.getYSize()/2)*0.5))
        base.win.movePointer(0,int(base.win.getXSize()/2),int(base.win.getYSize()/2))
        return task.cont
    #eventual loading screen for my game
    def Load(whatLoading):
        menuScreen.hide()
        optionsScreen.hide()
        if whatLoading=="Play":
            Game.Play()
    #menu screen
    def Menu():
        global menuScreen
        menuScreen=DirectDialog(frameSize=(0,0,0,0))
        nameText=OnscreenText(text="Duckwars:Beaks Of Rage",parent=menuScreen,scale=0.3,pos=(0,0.7),fg=(255,255,255,255),shadow=(0,0,0,255),font=font)
        playButton=DirectButton(text="Play",parent=menuScreen,scale=0.1,pos=(-1,0,0.3),frameSize=(-3,3,-0.4,0.9),command=Game.Load,extraArgs=["Play"])
        optionsButton=DirectButton(text="Options",parent=menuScreen,scale=0.1,pos=(-1,0,0.1),frameSize=(-3,3,-0.4,0.9),command=Game.Options)
        quitButton=DirectButton(text="Quit",parent=menuScreen,scale=0.1,pos=(-1,0,-0.1),frameSize=(-3,3,-0.4,0.9),command=Game.Quit)
    #options screen
    def Options():
        global optionsScreen
        optionsScreen=DirectDialog(frameSize=(-1.2,1.2,-0.7,0.7),pos=(0,0,-0.1))
        optionsText=OnscreenText(text="Options",parent=optionsScreen,scale=0.2,pos=(0,0.5,0),font=font)
        doneButton=DirectButton(text="Done",parent=optionsScreen,scale=0.1,pos=(-0.2,0,-0.6),command=optionsScreen.hide)
        quitButton=DirectButton(text="Quit",parent=optionsScreen,scale=0.1,pos=(0.2,0,-0.6),command=Game.Quit)
    #where the main game loop will go
    def Play():
        taskMgr.add(Game.CameraMovement,"CameraMovement")
        environment=loader.loadModel("environment").reparentTo(render)
        base.camera.setPos(0,0,10)
        base.accept("escape",Game.Options)
        base.accept("w",Game.UpdateKeyMap,["forward",True])
        base.accept("w-up",Game.UpdateKeyMap,["forward",False])
        base.accept("s",Game.UpdateKeyMap,["backward",True])
        base.accept("s-up",Game.UpdateKeyMap,["backward",False])
        base.accept("a",Game.UpdateKeyMap,["leftStrafe",True])
        base.accept("a-up",Game.UpdateKeyMap,["leftStrafe",False])
        base.accept("d",Game.UpdateKeyMap,["rightStrafe",True])
        base.accept("d-up",Game.UpdateKeyMap,["rightStrafe",False])
    #closes game, but throws really nong error error(still closes game window, but not launcher)
    #may be problem with sys.exit()
    #SystemError: PyEval_EvalFrameEx returned a result with an error set
    #did not do this before the compter was restarted
    def Quit():
        base.graphicsEngine.removeAllWindows()
        sys.exit()
#runs game
game=Game()
game.run()
