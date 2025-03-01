from p5 import *
from src.utilities.properties import *
from src.utilities.mouse import getMousePosition

W,H = getScreenSize()
player_size = getPlayerSize()

def render(translations):
    px,py = W/2,H/2
    mouse_x,mouse_y = getMousePosition()
    
    X = px - mouse_x
    Y = py - mouse_y

    angle = atan2(Y,X)

    translate(translations[0]+px,translations[1]+py)
    rotate(angle)
    rectMode(CENTER)
    fill(0)
    rect(-6,0,player_size+5,5)
    
    fill(255,0,0)
    ellipse(0,0,player_size,player_size)

    
    