extends Node3D

#makes player
var player_scene=preload("res://Player/Player.tscn")
var player=player_scene.instantiate()

#makes enemy
var enemy_scene=preload("res://Enemy/Enemy.tscn")
var enemy=enemy_scene.instantiate()
#for enemy spawing location
var enemySpawnTimer=10
var enemySpawnTimerAdd=10
@onready var enemySpawner=$"Enemy Spawner"

func _ready():
	#spawns in player when game is started
	add_child(player)
	#moves player to the ground
	player.position.x=10
	#hides mouse
	Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)
	
#closes game when escape key is pressed
func _input(event):
	if event is InputEventKey and event.pressed:
		if event.keycode==KEY_ESCAPE:
			get_tree().quit()
			
func _process(_delta):
	if player.timeAlive+10>=enemySpawnTimer:
		enemy=enemy_scene.instantiate()
		add_child(enemy)
		enemy.position=enemySpawner.position
		enemySpawnTimer+=enemySpawnTimerAdd
		enemySpawnTimerAdd-=0.1
	get_tree().call_group("Enemys","update_target_location",player.global_transform.origin)
