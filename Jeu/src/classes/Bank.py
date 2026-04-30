from p5 import *
from src.utilities.properties import getScreenSize


class Bank:
    def __init__(self):
        self.screen_w, self.screen_h = getScreenSize()
        self.gold: int = 100
        self.silver: int = 100
        self.bronze: int = 100

    def Afficher_banque(self):
        fill(0)
        text_size(15)
        text(f"G={self.gold}", self.screen_w * 0.4, 90)
        text(f"S={self.silver}", self.screen_w * 0.5, 90)
        text(f"B={self.bronze}", self.screen_w * 0.6, 90)


Purse = Bank()
