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
        global font
        #inits showbase
        ShowBase.__init__(self)
        #disables default camera controls
        self.disableMouse()
        #gets window properties
        wp=WindowProperties()
        #sets size
        wp.setSize(base.pipe.getDisplayWidth(),base.pipe.getDisplayHeight())
        base.win.requestProperties(wp)
        #makes font
        font=loader.loadFont('font.ttf')
        font.setPixelsPerUnit(100)
        font.setPageSize(512,512)
        #inits options screen
        Game.Options()
        optionsScreen.hide()
        #inits and opens menu
        Game.Menu()
    def Load(whatLoading):
        if whatLoading=="Play":
            menuScreen.hide()
            optionsScreen.hide()
            Game.Play()
    def Menu():
        global menuScreen
        menuScreen=DirectDialog(frameSize=(0,0,0,0))
        nameText=OnscreenText(text="Duckwars:Beaks Of Rage",parent=menuScreen,scale=0.3,pos=(0,0.7),fg=(255,255,255,255),shadow=(0,0,0,255),font=font)
        playButton=DirectButton(text="Play",parent=menuScreen,scale=0.1,pos=(-1,0,0.3),frameSize=(-3,3,-0.4,0.9),command=Game.Load,extraArgs=["Play"])
        optionsButton=DirectButton(text="Options",parent=menuScreen,scale=0.1,pos=(-1,0,0.1),frameSize=(-3,3,-0.4,0.9),command=Game.Options)
        quitButton=DirectButton(text="Quit",parent=menuScreen,scale=0.1,pos=(-1,0,-0.1),frameSize=(-3,3,-0.4,0.9),command=Game.Quit)
    def Options():
        global optionsScreen
        optionsScreen=DirectDialog(frameSize=(-1.2,1.2,-0.7,0.7),pos=(0,0,-0.1))
        doneButton=DirectButton(text="Done",parent=optionsScreen,scale=0.1,pos=(-0.2,0,-0.6),command=optionsScreen.hide)
        quitButton=DirectButton(text="Quit",parent=optionsScreen,scale=0.1,pos=(0.2,0,-0.6),command=Game.Quit)
    def Play():
        environment=loader.loadModel("environment").reparentTo(render)
    def Quit():
        base.graphicsEngine.removeAllWindows()
        sys.exit()
#runs game
game=Game()
game.run()



