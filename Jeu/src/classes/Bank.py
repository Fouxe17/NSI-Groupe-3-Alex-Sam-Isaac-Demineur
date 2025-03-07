from p5 import *
from src.utilities.properties import getScreenSize

class Bank:
    def __init__(self):
        self.screen_w, self.screen_h = getScreenSize()
        self.Gold:int= 100
        self.Silver:int = 100
        self.Bronze:int = 100
    
    def Afficher_banque(self):
        fill(0)
        text_size(15)
        text(f"G={self.Gold}", self.screen_w * 0.4 , 90)
        text(f"S={self.Silver}", self.screen_w * 0.5, 90)
        text(f"B={self.Bronze}", self.screen_w * 0.6 , 90)

Purse=Bank()