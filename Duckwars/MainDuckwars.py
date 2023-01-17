#imports
from direct.showbase.ShowBase import ShowBase
from panda3d.bullet import *
from panda3d.core import *
from direct.task import Task

#Game Class
class Game(ShowBase):
  #initializes game things
  def __init__(self):
    #sets globals variables
    global bulletWorld,wp
    #initializes the game window
    ShowBase.__init__(self)
    #inits physics simulation and gravity
    bulletWorld=BulletWorld()
    bulletWorld.setGravity(Vec3(0,0,-9.81))
    #gets window properties
    wp=WindowProperties()
    #sets size
    width=base.pipe.getDisplayWidth()
    height=base.pipe.getDisplayHeight()
    wp.setSize(width,height)
    base.win.requestProperties(wp)
    #calls play function
    Game.Play()
    #disables mouse controlls
    base.disableMouse()
  #hides mouse
  def mouseHide():
    wp.setCursorHidden(True)
    base.win.requestProperties(wp)
  #shows mouse
  def mouseShow():
    wp.setCursorHidden(False)
    base.win.requestProperties(wp)
  #updates the physics simulation every frame
  def updatePhys(task):
    bulletWorld.doPhysics(globalClock.getDt())
    return task.cont
  #player movement task,
  def playerMovement(task):
    base.camera.setP(base.camera,base.win.getPointer(0).getY()-int(base.win.getYSize()/2))
    playerNode.setH(playerNode,base.win.getPointer(0).getX()-int(base.win.getXSize()/2))
    base.win.movePointer(0,base.win.getXSize()//2,base.win.getYSize()//2)
    playerNode.setR(0)
    return task.cont
  #procedurally makes collision mesh for models
  def modelHBMakeRender(inputModel,mass,friction,pos):
    #inputs model
    inputModel=loader.loadModel(inputModel)
    #inits tirangle meshes
    outputBulletMesh=BulletTriangleMesh()
    #makes tiangle mesh be the shape of the geom and finds geom
    outputBulletMesh.addGeom(inputModel.findAllMatches("**/+GeomNode").getPath(0).node().getGeom(0))
    #makes charecter controller or rigidbody
    np=render.attachNewNode(BulletRigidBodyNode(str(inputModel)))
    #sets its starting position
    np.setPos(pos)
    #sets mass for the mesh
    np.node().setMass(mass)
    np.node().setFriction(friction)
    #adds mesh to the node
    np.node().addShape(BulletTriangleMeshShape(outputBulletMesh,dynamic=True))
    #renders and attaches mesh to node
    bulletWorld.attachRigidBody(np.node())
    #returns model and np
    return inputModel,np,
  #play function where gameplay will go
  def Play():
    global playerNode
    #makes collider debugand shows it
    debugNode=BulletDebugNode("debug")
    debugNode.showBoundingBoxes(True)
    debugNP = render.attachNewNode(debugNode)
    debugNP.show()
    bulletWorld.setDebugNode(debugNP.node())
    #adds mesh and renders boxing ring
    boxingRing,boxingRingNode=Game.modelHBMakeRender("Models/BoxingRing.glb",0,1,(0,0,-2))
    boxingRing.reparentTo(boxingRingNode)
    #Adds mesh and renders player
    player,playerNode=Game.modelHBMakeRender("Models/Player.glb",1,1,(0,0,0))
    player.reparentTo(playerNode)
    #reparents camera to player and sets position to the head
    #base.oobe()
    base.camera.reparentTo(playerNode)
    base.camera.setPos(0,1,1)
    #sets cursor to middle
    base.win.movePointer(0,base.win.getXSize()//2,base.win.getYSize()//2)
    #starts the physics
    taskMgr.add(Game.updatePhys,"updatePhys",sort=1)
    taskMgr.add(Game.playerMovement,"playerMovement",sort=2)
    #Game.mouseHide()
#runs the game
game=Game()
game.run()