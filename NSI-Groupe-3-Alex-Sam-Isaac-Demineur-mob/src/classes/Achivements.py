from p5 import *
from src.classes.Reward import *
from src.classes.Bank import *

class Achievement:
    def __init__(self, title, reward, completed=False):
        self.title = title
        self.reward:Reward = reward
        self.completed = completed
        self.collected = False

    def draw_achievement(self, x, y):
        rectMode(CORNER)
        fill(200 if self.completed else 100)
        rect(x, y, 300, 50)
        fill(0)
        text_size(16)
        text(f"{self.title}", x + 150, y + 25)

    def collect_reward(self):
        if self.completed and not self.collected:
            print(f"Récompense '{self.reward}' collectée!")
            self.collected = True
            Purse.Gold += self.reward.Gold
            Purse.Silver += self.reward.Silver
            Purse.Bronze += self.reward.Bronze
        print(f"Gold = '{Purse.Gold}' , Silver = '{Purse.Silver}' , Bronze = '{Purse.Bronze}'")