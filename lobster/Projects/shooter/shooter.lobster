//imports
import gl
import color
import vec

//inits window
gl_window("Shooter",500,500)
//loads font
gl_set_font_name("data/fonts/US101/US101.ttf")
gl_set_font_size(32)

// global vairbales
let origin=float(gl_window_size())/2.0
let worldScaler=20
var isPlaying=false
var getUpgrade=false
var upgradeNum=10
//loads soundtrack for less lag
load_ogg("soundTrack.ogg")
//loads textures for upgrade buttons
let health=gl_load_texture("health.png")
assert health
let speed=gl_load_texture("speed.png")
assert speed
let upgradeText=gl_load_texture("upgradeNum.png")
assert upgradeText

//bullet vairables
var bullets=[]

//enemy variables
var enemys=[]
var enemySpawnTime=gl_time()
var enemySpawnRate=0.1

//background particle variables
var particles=[]

//makes class for player
class player:
    pos:xy_f
    health:float
    speed:float
    nextPoint:int
    score:int
    highScore:int
    shots:int
    //for movement and drawing of player
    def drawMove(mousePos,worldSize):
        //key detection
        let dir=xy_f{(gl_button("a")>=1)-(gl_button("d")>=1),(gl_button("w")>=1)-(gl_button("s")>=1)}
        //for pointing player to mouse
        drawPointyTriangle(pos,mousePos,lerp(color_green,color_white,div(nextPoint-score,100)),3)
        //return directin for movt
        return dir 

//makes class for bullet
class bullet:
    pos:xy_f
    dir:xy_f
    speed:int
    //for movement and drawing of bullet
    def drawMove():
        pos+=dir*gl_delta_time()*speed
        gl_translate(pos):
            gl_color(color_yellow)
            gl_circle(0.2,100)

//makes class for enemy
class enemy:
    pos:xy_f
    dir:xy_f
    speed:int
    hp:int
    //for drawing and moving enemy
    def drawMove(pPos):
        let playerdir=normalize(pPos-pos)
        pos+=playerdir*gl_delta_time()*speed
        drawPointyTriangle(pos,playerdir,lerp(color_black,color_red,div(hp,2)),3)

//makes class for background particles
class particle:
    pos:xy_f

//makes player
let player=player{xy_0,100.0,10.0,100,0,0,1}

//function for drawing enemy/player
def drawPointyTriangle(pos,pointTo,color,points):
    gl_translate(pos):
        gl_rotate_z(pointTo):
            gl_color(color)
            if points==3:gl_polygon([xy_f{-0.5,0.5},xy_x,xy_f{-0.5,-0.5}])
            else:gl_circle(1.0,points)

//function for upgrade buttons
def upgradeButton(whatUpgrade,mousePos,pos,size,texture):
    //moves button
    gl_translate(pos):
        //makes normal colored button
        gl_color(color_green)
        //what happnes if the mouse is inside the button
        if mousePos.x>pos.x-size.x and mousePos.x<pos.x+size.x and mousePos.y>pos.y-size.y and mousePos.y<pos.y+size.y:
            //changes button color to red
            gl_color(color_red)
            //what happens if the player cliks the button
            if gl_button("mouse1")>0:
                play_wav("buttonClick.wav",0,2)
                if whatUpgrade=="health":player.health+=upgradeNum
                if whatUpgrade=="speed":player.speed+=div(upgradeNum,10)
                if whatUpgrade=="upgradeNum":upgradeNum+=5
                player.nextPoint*=2
                enemySpawnTime=gl_time()    
                getUpgrade=false
        //actually draws the button
        gl_rect(size,1)
        //draws image onto texture
        gl_set_shader("textured")
        gl_set_primitive_texture(0,texture)
        gl_color(color_white)
        gl_rect(size,1)
        gl_set_shader("color")

//runloop, needed for window to open
while gl_frame() and gl_button("escape")==0:

    //test
    gl_cull_front(false)

    //fills screen
    gl_clear(color_black)

    //plays song if it isnt already playing
    if sound_status(1)==0:sound_volume(play_ogg("soundTrack.ogg",0,1),0.3)

    //draws circle around mouse
    let worldSizes=gl_window_size().y/worldScaler
    gl_scale(worldSizes):
        gl_translate(gl_local_mouse_pos(0)):
            gl_line_mode(1):
                gl_color(color_grey)
                gl_circle(0.5,20)

    //Sets color for drawing
    gl_color(color_white)

    //for starting the game
    if isPlaying==false:

        //start game message
        let startMsg="Press Space to Play!"
        //move message to middle of screen
        gl_translate((float(gl_window_size()-gl_text_size(startMsg)))/2.0):gl_text(startMsg)

        //highschore message
        let highScoreMsg="Your HighScore is {ceiling(player.highScore)}"
        gl_translate((float(gl_window_size()-gl_text_size(highScoreMsg)))/1.2):gl_text(highScoreMsg)

        //what happens when game is started
        if gl_button("space")>0:
            play_wav("start.wav",0,2)
            player.score=0
            player.health=100.0
            player.shots=1
            player.pos=xy_0
            bullets=[]
            enemys=[]
            enemySpawnRate=1.0
            enemySpawnTime=gl_time()
            particles=[]
            for(20):particles.push(particle{xy_f{rnd_float()*12.0-rnd_float()*12.0,rnd_float()*12.0-rnd_float()*12.0}})
            isPlaying=true

    //main runloop
    if isPlaying==true and getUpgrade==false:

        //shows health, score and highschore
        let playMsg="Health: {ceiling(player.health)} - Score: {ceiling(player.score)}"
        //moves it to the top left corner
        gl_translate(float(gl_text_size(playMsg))/origin):gl_text(playMsg)

        //sets origin to center
        gl_translate(origin)

        //sets world scale
        let worldSize=gl_window_size().y/worldScaler
        gl_scale(worldSize)

        let toMouse=normalize(gl_local_mouse_pos(0)-player.pos)

        //draws player and moves player
        let moveDir=player.drawMove(toMouse,worldSize)

        //for getting upgrades
        if player.score==player.nextPoint:
            //plays upgrade sound
            play_wav("upgrade.wav",0,2)
            //switches to upgrade screen
            getUpgrade=true

        //for spawing in new particles needs to reset every frame
        var particlesonScreen=0

        //draws background particles
        for(particles) p:
            if magnitude(player.pos-p.pos)<12.0:
                particlesonScreen+=1
            gl_translate(p.pos):
                gl_color(color_white)
                gl_circle(0.05,6)
            p.pos+=moveDir*gl_delta_time()*player.speed
            //removes background particles that are too far
            if abs(p.pos.x)>worldScaler*10 or abs(p.pos.y)>worldScaler*10:remove_obj(particles,p)

        //adds more background particles
        if particlesonScreen<20:particles.push(particle{xy_f{rnd_float()*13.0-rnd_float()*13.0,rnd_float()*13.0-rnd_float()*13.0}})

        //for shooting bullets
        if gl_button("mouse1")==1:
            for(player.shots):
                bullets.push(bullet{player.pos,toMouse,20})
                play_wav("shoot.wav",0,2)

        //for drawing and moving bullets
        for(bullets) b:
            //draws and moves bullets
            b.drawMove()
            //moves bullets again
            b.pos+=moveDir*gl_delta_time()*player.speed
            //culls bullets that are too far
            if abs(b.pos.x)>worldScaler or abs(b.pos.y)>worldScaler:remove_obj(bullets,b)
        
        //spawns in enemys
        if enemySpawnTime<gl_time():
            enemys.push(enemy{sincos(rnd(360))*(worldSize/2),xy_0,8,2})
            enemySpawnTime+=enemySpawnRate
            enemySpawnRate*=0.999

        //for enemy drawing, moving, and bullet colisions/health and player health and restating the game
        for(enemys) e:
            //for enemy drawing and moving
            e.drawMove(player.pos)
            //for moving again
            e.pos+=moveDir*gl_delta_time()*player.speed
            //for player damaging
            if magnitude(player.pos-e.pos)<1.0:
                player.health-=gl_delta_time()*5.0
                //for resetting the game
                if player.health<=0.0:
                    sound_volume(play_wav("gameOver.wav",0,2),0.4)
                    player.highScore=max(player.highScore,player.score)
                    isPlaying=false
            //for bullet colision
            for(bullets) b:
                if magnitude(b.pos-e.pos)<1.0:
                    e.hp=max(e.hp-1,0)
                    remove_obj(bullets,b)
            //for enemys being removed when dead
            if e.hp==0:
                play_wav("enemyHurt.wav",0,2)
                remove_obj(enemys,e)
                player.score+=1

    //for getting upgrades
    if getUpgrade==true:

        //sets upgrade message
        let upgradeMsg="Select an Upgrade!"

        //move message to middle of screen
        gl_translate(float(gl_window_size()-gl_text_size(upgradeMsg))/2.0):gl_text(upgradeMsg) 

        //sets origin to center
        gl_translate(origin)

        //sets world scale
        let worldSize=gl_window_size().y/worldScaler
        gl_scale(worldSize)

        //makes mouse position
        let mousePos=gl_local_mouse_pos(0)

        //makes buttons and does the effect when you clock on it
        upgradeButton("health",mousePos,xy_f{4.0,-4.0},xy_f{2.0,2.0},health)
        upgradeButton("speed",mousePos,xy_f{-4.0,-4.0},xy_f{2.0,2.0},speed)
        upgradeButton("upgradeNum",mousePos,xy_f{0.0,4.0},xy_f{2.0,2.0},upgradeText)

    //mutes sound
    for(8) e:sound_volume(e,0.0)






