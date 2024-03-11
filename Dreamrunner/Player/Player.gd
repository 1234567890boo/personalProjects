extends CharacterBody3D


const SPEED=10.0
const JUMP_VELOCITY=10.0

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

#get screen size for mouse things
var mouseMovement=Vector2.ZERO
var centerOfScreen=DisplayServer.window_get_size()/2
var mouseSens=0.3

#for camera things
@onready var camera=$Camera3D
var cameraBob=0
var cameraBobSize=1

#player health
var HEALTH=100

#for time alive
var timeAlive=-10
@onready var timeAliveLabel=$UICamera/time_alive

#get camera for the hurt overlay
@onready var hurtImage=$UICamera/hurt

#for the dream bar
@onready var dreamBarLabel=$UICamera/DreamBarLabel
@onready var dreamBar=$UICamera/DreamBarLabel/DreamBar
var dreamMode=false

#for shooting
@onready var bulletSpawn=$Camera3D/bulletSpawn
@onready var arrow_scene=preload("res://Arrow.tscn")

#for control text fading
@onready var control=$UICamera/Controls
@onready var crosshair=$UICamera/Crosshair

#removes errors about up vector and direction being algned with enemy
func _ready():move_and_slide()
	
func _physics_process(delta):
	#for controll timer
	if timeAlive<0:crosshair.modulate.a=0
	if timeAlive>0:
		crosshair.modulate.a=100
		control.modulate.a=0
		dreamBar.value+=0.1
	#for time alive timer
	timeAlive+=delta
	timeAliveLabel.text="Time Alive:"+str(int(timeAlive))
	# Add the gravity.
	velocity.y -= gravity * delta

	# Handle Jump.
	if Input.is_action_pressed("jump") and is_on_floor():
		velocity.y=JUMP_VELOCITY

	# Get the input direction and handle the movement
	var input_dir=Input.get_vector("move_left", "move_right", "move_forward", "move_back")
	var direction=(transform.basis*Vector3(input_dir.x,0,input_dir.y)).normalized()
	if direction:
		velocity.x = direction.x*SPEED
		velocity.z = direction.z*SPEED
	else:
		velocity.x = move_toward(velocity.x,0,SPEED)
		velocity.z = move_toward(velocity.z,0,SPEED)
	move_and_slide()
	
	#for looking around
	mouseMovement=Vector2i(get_viewport().get_mouse_position())-centerOfScreen
	self.rotation_degrees.y-=mouseMovement.x*mouseSens
	camera.rotation_degrees.x-=mouseMovement.y*mouseSens
	if camera.rotation_degrees.x>=80 or camera.rotation_degrees.x<=-80:
		camera.rotation_degrees.x+=mouseMovement.y*mouseSens
	get_viewport().warp_mouse(centerOfScreen)
	
	#for making the camera bob
	camera.position.y+=sin(cameraBob)/cameraBobSize
	cameraBob+=0.1
	cameraBobSize=150
	if velocity!=Vector3.ZERO:
		cameraBob+=0.1
		cameraBobSize=50
		
	#for vignette showing how hurt you are
	hurtImage.modulate.a=(100-HEALTH)*0.01
	
	#for dreambar things
	dreamBarLabel.set_position(Vector2i(290,140))
	dreamBar.set_position(Vector2i(5,75))

	#
	if dreamBar.value>=100 and Input.is_action_just_pressed("ActivateDream"):dreamMode=true
	if dreamMode==true:
		dreamBar.value-=0.4
		if Input.is_action_just_pressed("shoot"):shoot()
	if dreamBar.value==0:dreamMode=false
	#for dying
	if HEALTH<=0:get_tree().quit()

#for shooting
func shoot():
	var arrow=arrow_scene.instantiate()
	add_sibling(arrow)
	arrow.transform=bulletSpawn.global_transform
	arrow.linear_velocity=bulletSpawn.global_transform.basis.z*-35
	arrow.whoShot="player"
