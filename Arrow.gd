extends RigidBody3D

#for shooting the player
@onready var player=get_parent().get_node("Player")

#for
var whoShot=null
#for dying
var deathTimer=1

func _process(delta):
	#for hurting player
	if global_position.distance_to(player.global_position)<1 and whoShot=="enemy":
		player.HEALTH-=10
		queue_free()
	#for killing enemy
	for enemy in get_tree().get_nodes_in_group("Enemies"):
		if global_position.distance_to(enemy.global_position)<1 and whoShot=="player":
			enemy.queue_free()
			player.HEALTH+=5
			if player.HEALTH>100:player.HEALTH=100
			queue_free()
	#for dying
	deathTimer-=delta
	if deathTimer<0:queue_free()
