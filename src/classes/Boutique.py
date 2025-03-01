from p5 import *
from src.classes.Button import *
from src.classes.Bank import Purse
from src.classes.Reward import *
from src.utilities.properties import changePlayerColor

class Article:
    def __init__(self, cost:Reward, but:Button, type):
        self.cost=cost
        self.button = but
        self.buy = False
        self.type = type 

    def draw_article(self):
        self.button.draw()

    def Achat(self):
        pass

Boutique =[Article(Reward(B=10,G=10),Button(70,120,50,50,None,changePlayerColor((212,0,255)),color=(212,0,255)),"clr"),
           Article(Reward(S=8),Button(140,120,50,50,None,changePlayerColor((153,249,255)),color=(153,249,255)),"clr")
           ]

