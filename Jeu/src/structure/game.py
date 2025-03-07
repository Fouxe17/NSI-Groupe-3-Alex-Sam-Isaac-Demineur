from p5 import *
from random import *
from math import log1p

import src.utilities.properties as properties
import src.designs.player as d_player
import src.physics.player as p_player
import src.designs.block as block
import src.utilities.tweening as tweening
import src.classes.Mob as mobs_class
import src.utilities.mouse as mouse
import src.handling.projectiles.bullet as bullet
import src.utilities.data as data

main_inter_x = tweening.AddLinearInterpolation(0,0,.1)
main_inter_y = tweening.AddLinearInterpolation(0,0,.1)

shake_x = tweening.AddLinearInterpolation(0,0,.1)
shake_y = tweening.AddLinearInterpolation(0,0,.1)
shake_strength = 0

distance_factor = 10
W,H = properties.getScreenSize()
current_data = data.get_rows()[0] #Data n°1

main_game_infos = {
    "CanShoot": True,
    "Clicking":False,
    "ClickState":False,
    "WatchingAngle": 0,
    "SessionKills":0,
    "Score": 0,
    "BestScore": current_data[1] #Le meilleur score
    }

offset_position = [0,0]
plrp = [0,0]

spawn_tick = 0
spawn_rate = .5 #Un mob chaque x secondes
spawning_range = 1000 #Les mobs peuvent spawn sur x pixels
mob_colors = [
    [9, 255, 0],
    [255, 33, 100],
    [0, 255, 76],
    [255, 128, 0],
    [56, 29, 1],
    [0, 51, 255],
    [204, 0, 255]
]

def setupGame():
    global main_game_infos,spawn_rate, plrp
    main_game_infos = {
    "CanShoot": True,
    "Clicking":False,
    "ClickState":False,
    "WatchingAngle": 0,
    "SessionKills":0,
    "Score": 0,
    "BestScore": current_data[1] #Le meilleur score
    }
    mobs_class.current_mobs = []
    spawn_rate = .5
    shake_x.reset()
    shake_y.reset()
    plrp = [0,0]

def spawn_mob():
    get_random_pos = lambda : random() * choice([-1,1]) * spawning_range
    taille = uniform(7,30)
    santé = taille * 1 / 8
    mobs_class.Mobs(
        get_random_pos(), get_random_pos(),
        {
            "Vitesse": uniform(1,1.5) * 2,
            "Taille": taille,
            "Couleur": choice(mob_colors),
            "SantéMax": santé,
            "Santé": santé,
            "Score": randint(5,10)
        }
        )

def draw_game():
    global offset_position,plrp,spawn_tick,spawn_rate,shake_strength
    background(0)
    main_game_infos["Clicking"] = mouse.onClickEvent() #Si la souris est appuyée
    main_game_infos["ClickState"] = mouse.getMousePressed()

    tweening.draw_update()
    mouse.update()

    if spawn_tick < millis():
        spawn_tick = millis() + spawn_rate * 1000
        spawn_mob()
        
    wdu2Da,n_plrp,alv = p_player.updatePlayerPosition()

    main_inter_x.A = offset_position[0]
    main_inter_x.B = wdu2Da[0] * distance_factor

    main_inter_y.A = offset_position[1]
    main_inter_y.B = wdu2Da[1] * distance_factor

    main_inter_x.play()
    main_inter_y.play()
    
    if main_game_infos["Clicking"]:
        shake_strength += 50

    shake_y.B = uniform(-shake_strength,shake_strength)
    shake_x.B = uniform(-shake_strength,shake_strength)

    shake_x.play()
    shake_y.play()
    
    translations = [-main_inter_x.progression + shake_x.progression,main_inter_y.progression + shake_y.progression]
    if shake_strength > 0:
        shake_strength -=10
    translate(translations[0],translations[1])
    collided = block.render(plrp)
    main_game_infos["WatchingAngle"] = d_player.render(main_game_infos["Clicking"])
    has_shot = bullet.render(main_game_infos,plrp)
    bullet.bullets, finished = mobs_class.update_render(plrp,bullet.bullets,main_game_infos)

    if has_shot:
        shake_strength += 40

    idx = 0
    for i in collided:
        is_not_colliding = i == 0
        result = is_not_colliding
        if not is_not_colliding:
            if wdu2Da[idx] == i:
                result = True
                alv[idx] = .5 * i
        if result:
            plrp[idx] += alv[idx]
        idx += 1

    offset_position[0] = main_inter_x.progression
    offset_position[1] = main_inter_y.progression

    spawn_rate = max(.1,4 - (.01 * main_game_infos["Score"]))

    reset_matrix()
    text_align(CORNER)
    t_size = 30
    fill(255)
    text_size(t_size)
    text("Score: "+str(main_game_infos["Score"]),0,H - t_size)

    if finished:
        if main_game_infos["Score"] > int(main_game_infos["BestScore"]):
            data.set_best_score(1,str(main_game_infos["Score"]))
            main_game_infos["BestScore"] = str(main_game_infos["Score"])

    return finished,main_game_infos