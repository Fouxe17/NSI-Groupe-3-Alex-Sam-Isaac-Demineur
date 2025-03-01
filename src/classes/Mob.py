from src.designs.mob import *
import src.physics.player as p_player
from src.physics.dist import getPlayerPos
from src.utilities.properties import getScreenSize

W,H = getScreenSize()
plrp=getPlayerPos()
class Mobs:
    def __init__(self, x:int, y:int):
        self.x=x
        self.y=y
        self.vitesse=1
    
    def draw_mobs(self):
        draw_mob(self.x,self.y)

    def goTo(self):
        # Calculer la direction
        dx = plrp[0]- self.x
        dy = plrp[1]- self.y
        distance = (dx**2 + dy**2) ** 0.5

        if distance > self.vitesse:
            self.x += (dx / distance) * self.vitesse
            self.y += (dy / distance) * self.vitesse
        else:
            self.x, self.y = plrp[0], plrp[1]

def update_render(nplrp:list[int,int]):
    global plrp
    plrp = nplrp