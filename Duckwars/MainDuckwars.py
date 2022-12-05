#imports
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
        #gets window properties
        wp=WindowProperties()
        #sets size
        wp.setSize(base.pipe.getDisplayWidth(),base.pipe.getDisplayHeight())
        self.win.requestProperties(wp)
        #makes font
        font=loader.loadFont('font.ttf')
        #starts game by opening menu screen
        Game.Menu()
    def Menu():
        menuScreen=DirectDialog(frameSize=(0,0,0,0))
        nameText=OnscreenText(text="Duckwars:Beaks Of Rage",scale=0.3,pos=(0,0.7),fg=(255,255,255,255),font=font)
#runs game
game=Game()
game.run()
