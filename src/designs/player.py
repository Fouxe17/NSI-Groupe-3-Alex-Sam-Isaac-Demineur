from p5 import *
from src.utilities.properties import *
from src.utilities.tweening import *

main_inter_x = AddLinearInterpolation(0,0,.1)
main_inter_y = AddLinearInterpolation(0,0,.1)

W,H = getScreenSize()
player_size = getPlayerSize()

offset_position = [0,0]
distance_factor = 10

def render(position=[0,0]):
    global offset_position
    fill(255,0,0)

    main_inter_x.A = offset_position[0]
    main_inter_x.B = position[0] * distance_factor

    main_inter_y.A = offset_position[1]
    main_inter_y.B = position[1] * distance_factor

    main_inter_x.play()
    main_inter_y.play()
    
    ellipse(W/2 - main_inter_x.progression,H/2 + main_inter_y.progression,player_size,player_size)