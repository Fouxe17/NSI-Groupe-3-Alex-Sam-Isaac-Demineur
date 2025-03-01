from p5 import *
import src.designs.player as d_player
import src.physics.player as p_player
import src.designs.block as block
import src.utilities.tweening as tweening
import src.classes.Mob as mobs_class
main_inter_x = tweening.AddLinearInterpolation(0,0,.1)
main_inter_y = tweening.AddLinearInterpolation(0,0,.1)

distance_factor = 10

offset_position = [0,0]
monsters=[mobs_class.Mobs(300,300),mobs_class.Mobs(600,200)]
def mobs():
    
    for mob in monsters:
        mob.draw_mobs()
        mob.goTo()

def draw_game():
    global offset_position
    background(125)
    tweening.draw_update()
    
    new_pos,plrp = p_player.updatePlayerPosition()

    main_inter_x.A = offset_position[0]
    main_inter_x.B = new_pos[0] * distance_factor

    main_inter_y.A = offset_position[1]
    main_inter_y.B = new_pos[1] * distance_factor

    main_inter_x.play()
    main_inter_y.play()

    translations = [-main_inter_x.progression,main_inter_y.progression]
    translate(translations[0],translations[1])

    block.render(plrp)
    mobs_class.update_render(plrp)
    mobs()
    d_player.render(translations)
    

    offset_position[0] = main_inter_x.progression
    offset_position[1] = main_inter_y.progression