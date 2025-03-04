from p5 import *
from src.utilities.properties import *
from src.utilities.misc import clamp

W,H = getScreenSize()
player_size = getPlayerSize() #Qui est aussi caractérisé par son rayon.
last_collision = "None"

blocks = []

class AddBlock:
    def __init__(self,x=0,y=0,sx=10,sy=10,settings={}):
        self.x = W/2 + x
        self.y = H/2 + y
        self.sx = sx
        self.sy = sy
        
        original_settings = {
            "BlockColor": [0 for i in range(3)],
            "Render":True,
            "Collidable":True
        }
        settings_fusion = None
        if len(settings) == 0:
            settings_fusion = original_settings
        else:
            settings_fusion = original_settings | settings
        self.settings = settings_fusion

        blocks.append(self)

    def render(self,plrp,collide_result:list[int,int]):
        if not self.settings["Render"]: return
        rectMode(CORNER)
        col = self.settings["BlockColor"]
        fill(col[0],col[1],col[2])
        x_coor = self.x - plrp[0]
        y_coor = self.y + plrp[1]
        rect(x_coor,y_coor,self.sx,self.sy)
        if self.settings["Collidable"]:
            # MAX_SX = self.sx/2
            # MAX_SY = self.sy/2
                
            # dist_x = abs((x_coor - W/2))
            # dist_y = abs((y_coor - H/2))

            # rect_x = clamp(dist_x,0,MAX_SX)
            # rect_y = clamp(dist_y,0,MAX_SY)

            # relative_distance = sqrt(rect_x**2 + rect_y**2)
            # absolute_distance = sqrt(dist_x**2 + dist_y**2)

            # print(absolute_distance - relative_distance)
            # if relative_distance == absolute_distance:
            #     # print("IN SIUU")
            #     pass

            xc = plrp[0] + W/2
            yc = H/2 - plrp[1]

            closest_x = max(self.x,min(xc,self.x + self.sx))
            closest_y = max(self.y,min(yc,self.y + self.sy))
            
            c_dist = math.sqrt((xc - closest_x) ** 2 + (yc - closest_y) ** 2)
            # print(plrp[0] + W/2,self.x)
            # print(H/2- plrp[1], self.y)

            collided = c_dist <= player_size/2
            
            if collided:
                if self.x < xc < self.x + self.sx:
                    
                    # print(yc - self.y,(self.y + self.sy) - yc)
                    if (yc - self.y) < (self.y + self.sy) - yc:
                        collide_result[1] = 1
                    else:
                        collide_result[1] = -1
                if self.y < yc < self.y + self.sy:
                    
                    if (xc - self.x) > (self.x + self.sx) - xc:
                        collide_result[0] = 1
                    else:
                        collide_result[0] = -1
                #Essai grâce à la détection des quatres sommets du rectangle
                # points = [
                #     [self.x, self.y], #HG
                #     [self.x + self.sx, self.y], #HD
                #     [self.x + self.sx, self.y + self.sy], #BD
                #     [self.x, self.y + self.sy] #BG
                # ]
                # points_dists = []
                # orders = {}
                # count = 0
                # for i in points:
                #     dist = sqrt((xc - i[0])**2 + (yc - i[1])**2)
                #     string = str(dist)
                #     points_dists.append(dist)
                #     orders[string] = count
                #     count += 1
                # points_dists = sorted(points_dists)
                # print(orders[str(points_dists[0])],orders[str(points_dists[1])])
        return collide_result
def render(plrp):
    collide_result = [0,0]
    """Codes de résultat du collide:
    0 - Le joueur n'a touché aucun bloc.
    1 - Le joueur a touché un bloc.
    """  
    for i in blocks:
        collide_result = i.render(plrp,collide_result)
    return collide_result

AddBlock(x=50,y=-100,sx=500,sy=30)
# AddBlock(x=90,y=150,sx=100,sy=30)