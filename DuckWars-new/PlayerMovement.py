#imports
from bge import logic
#gets important things
cont=logic.getCurrentController()
owner=cont.owner
scene=logic.getCurrentScene()
objects=scene.objects
#gets cube 
cube=objects["Cube"]
#gets objects from logic bricks
Forward=cont.sensors["Forward"]
Backwards=cont.sensors["Backwards"]
#simple movement logic
if Forward.positive:
    cube.position.x+=1
if Backwards.positive:
    cube.position.x-=1