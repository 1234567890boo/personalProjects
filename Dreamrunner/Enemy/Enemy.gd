extends CharacterBody3D

@onready var nav:NavigationAgent3D=$NavigationAgent3D
@onready var player=get_parent().get_node("Player")
@onready var arrow_scene=preload("res://Arrow.tscn")
@onready var arrowSpawn=$BulletSpawn

#for moving
var SPEED=5.0
var ACEL=10.0

#for shooting
var shoot_timer=3.0

#test
func _ready():
	add_to_group("Enemies")
	
func _physics_process(delta):
	#for movement
	var direction=Vector3()
	nav.target_position=player.global_position
	direction=(nav.get_next_path_position()-global_position).normalized()
	velocity=velocity.lerp(direction*SPEED,ACEL*delta)
	#for pointing twords player
	look_at(player.position)
	self.rotation.x=0
	self.rotation.z=0
	#actualy moves enemy
	move_and_slide()
	#hurting player
	if global_position.distance_to(player.global_position)<2.5:player.HEALTH-=0.3
	#for shooting the player if too far away
	shoot_timer-=delta
	if shoot_timer<0:
		arrowSpawn.look_at(player.position)
		shoot()
		shoot_timer=3
		
func shoot():
	var arrow=arrow_scene.instantiate()
	add_sibling(arrow)
	arrow.transform=arrowSpawn.global_transform
	arrow.linear_velocity=arrowSpawn.global_transform.basis.z*-35
	arrow.whoShot="enemy"
