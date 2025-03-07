from p5 import *
from src.utilities.properties import *

W,H = getScreenSize()
sHypo = getScreenHypotenuse()
bullets = []
pooling_max_lenght = 5

spawn_rate = .2
current_tick = 0

class Add:
    def __init__(self,x:int,y:int,angle=0,settings={}):
        """Ajoute un objet de type Bullet. A noter que cette classe utilise le Object Pooling"""
        self.x = x + W/2
        self.y = y + H/2
        self.angle = angle
        self.color = (255, 102, 13)

        original_settings = {
            "Render":True,
            "Size": 10,
            "Damages": 1,
            "SpeedFactor": 10, #x pixels per frame
            "Piercing": True, #Si elle pas transpercer des mobs
            "DamagesDealt": 1, #Les damages du bullet
            "Hits": [], # Liste qui se remplit des monstres que la balle a touché.
        }
        settings_fusion = None
        if len(settings) == 0:
            settings_fusion = original_settings
        else:
            settings_fusion = original_settings | settings
        self.settings = settings_fusion

        bullets.append(self)
        
    def render(self,plrp):
        self.color = getBulletColor()
        if not self.settings["Render"]: return
        sets = self.settings
        size = sets["Size"]
        angle = self.angle
        self.x += cos(angle) * sets["SpeedFactor"]
        self.y += sin(angle) * sets["SpeedFactor"]

        dx = self.x - W/2 - plrp[0]
        dy = self.y- H/2 + plrp[1]

        bullet_distance = sqrt(dx **2 + dy **2)
        if bullet_distance > sHypo/2: #on divie part deux puisqu'on part de la moitié de l'écran.
            self.settings["Render"] = False
            bullets.pop(bullets.index(self))

        fill(*self.color)
        ellipse(self.x - plrp[0], self.y + plrp[1],size,size)
    
def render(game_infos,plrp):
    global current_tick
    has_shot = False
    if game_infos["CanShoot"]:
        if game_infos["ClickState"]:
            if millis() > current_tick:
                current_tick = millis() + spawn_rate*1000
                Add(plrp[0],-plrp[1],game_infos["WatchingAngle"] + PI)
                has_shot = True
    noStroke()
    for i in bullets:
        i.render(plrp)
    stroke_weight(1)
    return has_shot