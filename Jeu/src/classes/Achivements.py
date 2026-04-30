from p5 import *
from src.classes.Bank import *
from src.classes.Reward import *

class Achievement:
    def __init__(self, title, reward, completed = False, goal = 10):
        self.title = title
        self.reward: Reward = reward
        self.completed = completed
        self.collected = False
        self.goal = goal

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
            purse.gold += self.reward.gold
            purse.silver += self.reward.silver
            purse.bronze += self.reward.bronze

        print(f"Gold = '{purse.gold}' , Silver = '{purse.silver}' , Bronze = '{purse.bronze}'")
