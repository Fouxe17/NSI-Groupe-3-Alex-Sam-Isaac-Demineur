from p5 import *
from src.classes.Button import *
from src.classes.Bank import Purse
from src.classes.Reward import *
from src.utilities.properties import *
from src.utilities.tweening import *

shooting_inter = AddLinearInterpolation(-6,-2,.2)

class Article:
    def __init__(self, cost:Reward, but:Button, type):
        self.cost=cost
        self.button = but
        self.buy = False
        self.type = type 
        self.state = False

    def draw_article(self):
        self.button.draw()
        if self.buy:
            self.button.text_size = 12
            self.button.text = "Acheté"

    def achat(self):
        if self.button.is_hovered(*getMousePosition()) and getMousePressed():
            if Purse.Gold >= self.cost.Gold and Purse.Silver >= self.cost.Silver and Purse.Bronze >= self.cost.Bronze and not self.buy :
                Purse.Gold -= self.cost.Gold
                Purse.Silver -= self.cost.Silver
                Purse.Bronze -= self.cost.Bronze
                self.buy = True
                print("achat")
                if self.type == "pclr":
                    changePlayerColor(self.button.color)
                elif self.type == "cclr":
                    changeCanonColor(self.button.color)
                elif self.type == "bclr":
                    changeBulletColor(self.button.color)
            elif self.buy:
                if self.type == "pclr":
                    changePlayerColor(self.button.color)
                elif self.type == "cclr":
                    changeCanonColor(self.button.color)
                elif self.type == "bclr":
                    changeBulletColor(self.button.color)

Boutique =[Article(Reward(G=10),Button(80,160,50,50,None,None,color=(212,0,255)),"pclr"),
           Article(Reward(G=10),Button(150,160,50,50,None,None,color=(153,249,255)),"pclr"),
           Article(Reward(G=10),Button(220,160,50,50,None,None,color=(67,128,0)),"pclr"),
           Article(Reward(G=10),Button(290,160,50,50,None,None,color=(67,128,182)),"pclr"),
           Article(Reward(G=10),Button(360,160,50,50,None,None,color=(143,128,182)),"pclr"),
           Article(Reward(G=10),Button(430,160,50,50,None,None,color=(228,116,43)),"pclr"),
           Article(Reward(G=10),Button(500,160,50,50,None,None,color=(85,255,140)),"pclr"),
           Article(Reward(G=10),Button(570,160,50,50,None,None,color=(113,85,140)),"pclr"),
           Article(Reward(S=20),Button(80,250,50,50,None,None,color=(212,0,255)),"cclr"),
           Article(Reward(S=20),Button(150,250,50,50,None,None,color=(153,249,255)),"cclr"),
           Article(Reward(S=20),Button(220,250,50,50,None,None,color=(67,128,0)),"cclr"),
           Article(Reward(S=20),Button(290,250,50,50,None,None,color=(67,128,182)),"cclr"),
           Article(Reward(S=20),Button(360,250,50,50,None,None,color=(143,128,182)),"cclr"),
           Article(Reward(S=20),Button(430,250,50,50,None,None,color=(228,116,43)),"cclr"),
           Article(Reward(S=20),Button(500,250,50,50,None,None,color=(85,255,140)),"cclr"),
           Article(Reward(S=20),Button(570,250,50,50,None,None,color=(113,85,180)),"cclr"),
           Article(Reward(B=30),Button(80,340,50,50,None,None,color=(212,0,255)),"bclr"),
           Article(Reward(B=30),Button(150,340,50,50,None,None,color=(153,249,255)),"bclr"),
           Article(Reward(B=30),Button(220,340,50,50,None,None,color=(67,128,0)),"bclr"),
           Article(Reward(B=30),Button(290,340,50,50,None,None,color=(67,128,182)),"bclr"),
           Article(Reward(B=30),Button(360,340,50,50,None,None,color=(143,128,182)),"bclr"),
           Article(Reward(B=30),Button(430,340,50,50,None,None,color=(228,116,43)),"bclr"),
           Article(Reward(B=30),Button(500,340,50,50,None,None,color=(85,255,140)),"bclr"),
           Article(Reward(B=30),Button(570,340,50,50,None,None,color=(113,85,180)),"bclr")]

def draw_joueur_test():
    player_color = getPlayerColor()
    canon_color = getCanonColor()
    px,py = 565,50
    mouse_x,mouse_y = getMousePosition()
    
    X = px - mouse_x
    Y = py - mouse_y

    angle = atan2(Y,X)
    push_matrix()
    translate(px,py)
    rotate(angle)
    rectMode(CENTER)
    fill(*canon_color)
    rect(shooting_inter.progression - 7,0,player_size+5,10)
    pop_matrix()
    fill(*player_color)
    ellipse(px,py,player_size,player_size)