from src.utilities.keyboard_handling import getPressedKeys
from src.utilities.misc import clamp

plrp = [0,0]
alv = [0,0]
watching_directional_unit__2D_angle: tuple[int,int] = [0,0]

max_speed = 2 #1 pixel par seconde
alv_factor = .05

key_map_H = {
    "d": 1, #Right
    "q":-1 #Left
}
key_map_V = {
    "z": 1, #Up
    "s":-1 #Down
}

def slow_down(x):
    if x == 0: return 0
    if round(abs(x),3) < .05:
        x = 0
    elif x > 0:
        x -= alv_factor
    elif x < 0:
        x += alv_factor
    return x

def updatePlayerPosition():
    global watching_directional_unit_2D_angle,plrp
    cu_keys = getPressedKeys()
    watching_directional_unit_2D_angle = [0,0]
    if len(cu_keys) > 0:
        watching_directional_unit_2D_angle = [
            clamp(sum(key_map_H[key] for key in cu_keys if key in key_map_H),-1,1),                                   
            clamp(sum(key_map_V[key] for key in cu_keys if key in key_map_V),-1,1)
        ]
    #Si on prend la valeur de l'index des key_map si on la touche est appuyée.
    for i in range(0,2):
        if watching_directional_unit_2D_angle[i] == 1:
            alv[i] += alv_factor
        elif watching_directional_unit_2D_angle[i] == -1:
            alv[i] -= alv_factor
        else:
            alv[i] = slow_down(alv[i])
        alv[i] = clamp(alv[i],-max_speed,max_speed)
    # plrp = [
    #     plrp[0] + alv[0],
    #     plrp[1] + alv[1]
    # ]
    # print(watching_directional_unit__2D_angle)
    return watching_directional_unit_2D_angle,plrp,alv
    