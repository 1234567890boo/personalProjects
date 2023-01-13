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
    global bulletWorld
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
  #updates the physics simulation every frame
  def updatePhys(task):
    bulletWorld.doPhysics(globalClock.getDt())
    return task.cont
  #procedurally makes collision mesh for models
  def modelHBMakeRender(inputModel,mass,pos):
    #inputs model
    inputModel=loader.loadModel(inputModel)
    #inits tirangle meshes
    outputBulletMesh=BulletTriangleMesh()
    #makes tiangle mesh be the shape of the geom and finds geom
    outputBulletMesh.addGeom(inputModel.findAllMatches("**/+GeomNode").getPath(0).node().getGeom(0))
    #attaches rigid body to the render
    np=render.attachNewNode(BulletRigidBodyNode(str(inputModel)))
    #sets its starting position
    np.setPos(pos)
    #sets mass for the mesh
    np.node().setMass(mass)
    #adds mesh to the node
    np.node().addShape(BulletTriangleMeshShape(outputBulletMesh,dynamic=True))
    #renders and attaches mesh to node
    bulletWorld.attachRigidBody(np.node())
    #returns model and np
    return inputModel,np
  #play function where gameplay will go
  def Play():
    global player
    #makes collider debugand shows it
    debugNode=BulletDebugNode("debug")
    debugNode.showBoundingBoxes(True)
    debugNP = render.attachNewNode(debugNode)
    debugNP.show()
    bulletWorld.setDebugNode(debugNP.node())
    #adds mesh and renders boxing ring
    boxingRing,boxingRingNode=Game.modelHBMakeRender("Models/BoxingRing.glb",0,(0,10,-2))
    boxingRing.reparentTo(boxingRingNode)
    #Adds mesh and renders player
    player,playerNode=Game.modelHBMakeRender("Models/Player.glb",1,(0,10,0))
    player.reparentTo(playerNode)
    #starts the physics
    taskMgr.add(Game.updatePhys,"updatePhys")
#runs the game
game=Game()
game.run()
