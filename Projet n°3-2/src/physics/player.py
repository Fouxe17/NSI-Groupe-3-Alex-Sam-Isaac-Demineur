from src.utilities.keyboard import getPressedKeys
plrp = [0,0]
watching_directional_unit__2D_angle: tuple[int,int] = [0,0]

speed = 1 #1 pixel par seconde

key_map_H = {
    "d": 1, #Right
    "q":-1 #Left
}
key_map_V = {
    "z": 1, #Up
    "s":-1 #Down
}

def updatePlayerPosition():
    global watching_directional_unit__2D_angle,plrp
    cu_keys = getPressedKeys()
    if len(cu_keys) == 0: return [0,0], plrp
    watching_directional_unit__2D_angle = [
        sum(key_map_H[key] for key in cu_keys if key in key_map_H),                                   
        sum(key_map_V[key] for key in cu_keys if key in key_map_V)
    ]
    plrp = [
        plrp[0] + watching_directional_unit__2D_angle[0]*speed,
        plrp[1] + watching_directional_unit__2D_angle[1]*speed
    ]
    #Si on prend la valeur de l'index des key_map si on la touche est appuyée.
    # print(watching_directional_unit__2D_angle)
    return watching_directional_unit__2D_angle,plrp
    