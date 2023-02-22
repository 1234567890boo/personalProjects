#imports
from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *
from panda3d.core import *
from direct.task import Task
#class with all game logic
class Game(ShowBase):
  #initializes game stuff
  def __init__(self):
    #inits window
    ShowBase.__init__(self)
    #inits game physics
    self.bulletWorld = BulletWorld()
    self.bulletWorld.setGravity(Vec3(0,0,-9.81))
    #inits window properties to change windwo size and cursor settings
    self.wp = WindowProperties()
    #changes screen size
    self.width = base.pipe.getDisplayWidth()
    self.height = base.pipe.getDisplayHeight()
    self.wp.setSize(self.width,self.height)
    #for testing
    self.wp.setSize(500,500)
    #actually sets screen size
    base.win.requestProperties(self.wp)
    #variables
    self.keyMap={"forward":False,"backward":False,"leftStrafe":False,"rightStrafe":False,"jump":False}
    #disables default mouse controls
    #base.disableMouse()
    base.oobe()
    #starts game
    self.Play()
  #task for updating physics
  def updatePhys(self, task):
    self.bulletWorld.doPhysics(globalClock.getDt())
    return task.cont
  #for updating keymap
  def updateKeyMap(self,key,toWhat):
    self.keyMap[key]=toWhat
  #task for player movement
  def playerMovement(self, task):
    #for camera mouse looking
    base.camera.setP(base.camera, base.win.getPointer(0).getY() - int(base.win.getYSize()/2))
    self.playerNode.setH(self.playerNode, base.win.getPointer(0).getX() - int(base.win.getXSize()/2))
    #moves cursor to center of screen
    base.win.movePointer(0, base.win.getXSize()//2, base.win.getYSize()//2)
    #camera movement capping
    if base.camera.getP()>80:base.camera.setP(79)
    if base.camera.getP()<-60:base.camera.setP(-61)
    if base.camera.getH()!= 0:base.camera.setH(0)
    #makes sure camera or player dont roll
    self.playerNode.setR(0)
    self.playerNode.setP(0)
    base.camera.setR(0)
    #for movement
    speed=Vec3()
    #checks if the player is on the ground
    canJump=self.bulletWorld.contactTest(self.playerNode.node()).getNumContacts()
    if canJump!=0:canJump=True
    #sets player movement based on keymap
    if self.keyMap["forward"]==True:speed+=Vec3(0,0.2,0)
    if self.keyMap["backward"]==True:speed+=Vec3(0,-0.2,0)
    if self.keyMap["rightStrafe"]==True:speed+=Vec3(0.1,0,0)
    if self.keyMap["leftStrafe"]==True:speed+=Vec3(-0.1,0,0)
    if self.keyMap["jump"]==True:speed+=Vec3(0,0,0.1)#not working
    #actually pushes player
    self.playerNode.setPos(self.playerNode,speed)
    #redos task
    return task.cont
  #makes physics mesh for models
  def modelHBMakeRender(self,inputModel,mass,friction,pos):
    #loads model
    inputModel=loader.loadModel(inputModel)
    #makes mesh thats empty
    outputBulletMesh=BulletTriangleMesh()
    for meshNum in range(0,len(inputModel.findAllMatches("**/+GeomNode")),1):
      #adds triangles to mesh that is the shape of the model
      outputBulletMesh.addGeom(inputModel.findAllMatches("**/+GeomNode").getPath(meshNum).node().getGeom(0))
    #adds rigid body node to render
    np=render.attachNewNode(BulletRigidBodyNode(str(inputModel)))
    #sets position of node
    np.setPos(pos)
    #sets mass of node
    np.node().setMass(mass)
    #sets friction of node
    np.node().setFriction(friction)
    #adds mesh to the node
    np.node().addShape(BulletTriangleMeshShape(outputBulletMesh,dynamic=True))
    #makes node have physics
    self.bulletWorld.attachRigidBody(np.node())
    #returns thigs i need for the future
    return inputModel, np
  #play function
  def Play(self):
    #makes colider mesh and other physics things show up
    self.debugNode=BulletDebugNode("debug")
    self.debugNode.showBoundingBoxes(True)
    self.debugNP=render.attachNewNode(self.debugNode)
    self.debugNP.show()
    self.bulletWorld.setDebugNode(self.debugNP.node())
    #makes boxing ring model and mesh and
    self.boxingRing,self.boxingRingNode=self.modelHBMakeRender("Models/BoxingRing.glb", 0, 1, (0,0,-2))
    self.boxingRing.reparentTo(self.boxingRingNode)
    #makes player mesh and model
    self.player, self.playerNode=self.modelHBMakeRender("Models/Player.glb", 1, 1, (0,0,0))
    self.player.reparentTo(self.playerNode)
    #makes camera follow player
    base.camera.reparentTo(self.playerNode)
    base.camera.setPos(0, 1, 1)
    #puts the cursor in the center of the screen
    base.win.movePointer(0, base.win.getXSize()//2, base.win.getYSize()//2)
    #starts the tasks
    taskMgr.add(self.updatePhys, "updatePhys", sort=1)
    taskMgr.add(self.playerMovement, "playerMovement", sort=2)
    #for player movement
    base.accept("w",self.updateKeyMap,extraArgs=["forward",True])
    base.accept("w-up",self.updateKeyMap,extraArgs=["forward",False])
    base.accept("s",self.updateKeyMap,extraArgs=["backward",True])
    base.accept("s-up",self.updateKeyMap,extraArgs=["backward",False])
    base.accept("a",self.updateKeyMap,extraArgs=["leftStrafe",True])
    base.accept("a-up",self.updateKeyMap,extraArgs=["leftStrafe",False])
    base.accept("d",self.updateKeyMap,extraArgs=["rightStrafe",True])
    base.accept("d-up",self.updateKeyMap,extraArgs=["rightStrafe",False])
    base.accept("space",self.updateKeyMap,extraArgs=["jump",True])
    base.accept("space-up",self.updateKeyMap,extraArgs=["jump",False])
#runs the game class
game = Game()
game.run()
