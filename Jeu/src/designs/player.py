from p5 import *
from src.utilities.properties import *
from src.utilities.tweening import *
from src.utilities.mouse import getMousePosition

shooting_inter = AddLinearInterpolation(-6,-2,.2)

W,H = getScreenSize()
player_size = getPlayerSize()

def render(clicked:bool):
    player_color = getPlayerColor()
    canon_color = getCanonColor()
    px,py = W/2,H/2
    mouse_x,mouse_y = getMousePosition()
    
    X = px - mouse_x
    Y = py - mouse_y

    angle = atan2(Y,X)

    if clicked:
        shooting_inter.B = -6
        shooting_inter.A = 3
        shooting_inter.reset()
        shooting_inter.play()

    push_matrix()
    translate(W/2,H/2)
    rotate(angle)
    rectMode(CENTER)
    fill(*canon_color)
    rect(shooting_inter.progression - 7,0,player_size+5,10)
    pop_matrix()
    fill(*player_color)
    ellipse(W/2,H/2,player_size,player_size)
    return angle
    
    