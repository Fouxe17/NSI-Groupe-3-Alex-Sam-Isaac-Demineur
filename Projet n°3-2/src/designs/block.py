from p5 import *
from src.utilities.properties import *
W,H = getScreenSize()

blocks = []

class AddBlock:
    def __init__(self,x=0,y=0,sx=10,sy=10,settings={}):
        self.x = W/2 + x
        self.y = H/2 + y
        self.sx = sx
        self.sy = sy
        
        original_settings = {
            "BlockColor": [0 for i in range(3)],
            "Render":True
        }
        settings_fusion = None
        if len(settings) == 0:
            settings_fusion = original_settings
        else:
            settings_fusion = original_settings | settings
        
        self.settings = settings_fusion

        blocks.append(self)

    def render(self,plrp):
        if not self.settings["Render"]: return
        rectMode(CENTER)
        col = self.settings["BlockColor"]
        fill(col[0],col[1],col[2])
        rect(self.x - plrp[0],self.y +plrp[1],self.sx,self.sy)

def render(plrp):
    for i in blocks:
        i.render(plrp)

AddBlock(x=50,y=-100,sx=500,sy=30)
AddBlock(x=90,y=150,sx=100,sy=30)