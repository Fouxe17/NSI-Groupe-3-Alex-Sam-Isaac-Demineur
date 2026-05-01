from p5 import *

import src.designs.player as d_player
import src.physics.player as p_player

import src.designs.block as block

import src.utilities.tweening as tweening

W,H=650,650

def setup():
    size(W,H)
    noStroke()
    
def draw():
    background(125)

    tweening.draw_update()
    

    new_pos,plrp = p_player.updatePlayerPosition()

    block.render(plrp)
    d_player.render(new_pos)

run()