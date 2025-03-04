from p5 import *
from random import *

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

distance_factor = 10
W,H = properties.getScreenSize()
current_data = data.get_rows()[0] #Data n°1

main_game_infos = {
    "CanShoot": True,
    "Clicking":False,
    "WatchingAngle": 0,
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
    global main_game_infos
    main_game_infos = {
    "CanShoot": True,
    "Clicking":False,
    "WatchingAngle": 0,
    "Score": 0,
    "BestScore": current_data[1] #Le meilleur score
    }
    mobs_class.current_mobs = []
    spawn_mob()

def spawn_mob():
    get_random_pos = lambda : random() * choice([-1,1]) * spawning_range
    taille = uniform(7,30)
    santé = taille * 1 / 10
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
    global offset_position,plrp,spawn_tick
    background(125)
    reset_matrix()
    text_align(CORNER)
    t_size = 30
    text_size(t_size)
    text("Score: "+str(main_game_infos["Score"]),0,H - t_size)
    main_game_infos["Clicking"] = mouse.onClickEvent() #Si la souris est appuyée

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

    translations = [-main_inter_x.progression,main_inter_y.progression]
    translate(translations[0],translations[1])

    main_game_infos["WatchingAngle"] = d_player.render(main_game_infos["Clicking"])
    bullet.bullets, finished = mobs_class.update_render(plrp,bullet.bullets,main_game_infos)
    bullet.render(main_game_infos,plrp)
    collided = block.render(plrp)
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

    if finished:
        if main_game_infos["Score"] > int(main_game_infos["BestScore"]):
            print("new best score !")
            data.set_best_score(1,str(main_game_infos["Score"]))
            main_game_infos["BestScore"] = str(main_game_infos["Score"])

    return finished,main_game_infos["Score"]