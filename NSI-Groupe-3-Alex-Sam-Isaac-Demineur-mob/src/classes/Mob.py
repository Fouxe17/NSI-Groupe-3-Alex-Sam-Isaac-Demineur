from p5 import *
import src.physics.player as p_player
from src.utilities.properties import getScreenSize,getPlayerSize

W,H = getScreenSize()

delta = .02
current_mobs = []

class Mobs:
    def __init__(self, x:int, y:int,settings={}):
        self.x=x+ W/2
        self.y=y+ H/2
        self.vitesse=1
        original_settings = {
            "Couleur": [9, 255, 0],
            "Visible":True,
            "InterpolationDelta": .005, #En gros la vitesse. L'idéal serait .02. Deprecated
            "Vitesse": 1.5,
            "SantéMax": 5,
            "Santé":5, #La santé actuaelle du mob
            "Taille": 15,
            "HPTailleX": 20, #Taille de la barre d'HP en X
            "HPTailleY": 7, #Taille de la barre d'HP en Y
            "Score": 5,
        }
        settings_fusion = None
        if len(settings) == 0:
            settings_fusion = original_settings
        else:
            settings_fusion = original_settings | settings
        self.settings = settings_fusion
        current_mobs.append(self)
    
    def draw_mob(self,plrp):
        sets = self.settings
        if not sets["Visible"]:
            return
        size = sets["Taille"]
        col = sets["Couleur"]
        fill(col[0],col[1],col[2])
        x = self.x - plrp[0]
        y = self.y + plrp[1]
        ellipse(x, y,size,size)
        if sets["Santé"] < sets["SantéMax"]:
            rectMode(CORNER)
            t = sets["HPTailleX"]
            height_offset = sets["Taille"] +2
            fill(0,255,0)
            frac = sets["Santé"]/sets["SantéMax"]
            rect(x - t/2, y-height_offset, frac*t, sets["HPTailleY"])
            fill(255,0,4)
            rect((x + frac*t) - t/2, y-height_offset, (1-frac)*t, sets["HPTailleY"])

    def update_physics(self,bullets:list,main_game_infos):
        for i in bullets:
            if self in i.settings["Hits"]:
                continue
            sets = i.settings
            dx = i.x - self.x
            dy = i.y - self.y
            distance = (dx**2 + dy**2) ** .5
            if distance < self.settings["Taille"]: #Le mob a été touché
                self.settings["Santé"] -= sets["DamagesDealt"]
                if self.settings["Santé"] <= 0:
                    main_game_infos["Score"] += self.settings["Score"]
                    current_mobs.pop(current_mobs.index(self))
                if not sets["Piercing"]:
                    bullets.pop(bullets.index(i))
                sets["Hits"].append(self)
                break
        return bullets

    def goTo(self,plrp):
        # Calculer la direction
        sets = self.settings
        dx = self.x - plrp[0] - W/2
        dy = -(plrp[1] - H/2) - self.y
        distance = sqrt(dx**2 + dy**2)
        touched = False
        if distance > getPlayerSize():
            angle = atan2(-(plrp[1] - H/2) - self.y,dx)
            self.x -= cos(angle) * sets["Vitesse"]
            self.y += sin(angle) * sets["Vitesse"]
            #Avec interpolation
            # self.x = self.x - dx * sets["InterpolationDelta"]
            # self.y = self.y + (-(plrp[1] - H/2) - self.y) * sets["InterpolationDelta"]
        else:
            touched = True
        return touched
        
def update_render(nplrp:list[int,int],bullets:list,main_game_infos):
    global plrp
    plrp = nplrp
    touched = False
    for mob in current_mobs:
        bullets = mob.update_physics(bullets,main_game_infos)
        t = mob.goTo(plrp)
        mob.draw_mob(plrp)
        if t:
            touched = True
    return bullets, touched