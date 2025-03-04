from p5 import *
from src.classes.Achivements import *
from src.classes.Button import *
import src.utilities.data as BDD_IMPORT
from src.utilities.mouse import *
from src.classes.Reward import *
from src.structure.game import *
from src.classes.Bank import *
from src.utilities.properties import getScreenSize
from src.classes.Boutique import *

previous_score = 0

class GameMenu:
    def __init__(self):
        self.state = "main menu"
        self.screen_w , self.screen_h = getScreenSize()
        self.start_button = None
        self.achievements_button = None
        self.back_button = None
        self.collect_buttons = []
        self.achievements = [
            Achievement("Premier Pas", Reward(10,G=100), completed=False),
            Achievement("Maître du Jeu", Reward(S=45, G=200), completed=True),
            Achievement("Champion", Reward(S=670, G=500), completed=True),
        ]

    def setup(self):
        size(self.screen_w, self.screen_h)
        self.update_layout()

    def update_layout(self):
        self.start_button = Button(self.screen_w // 2, self.screen_h // 2 - 200, 200, 60, "Start")
        self.achievements_button = Button(self.screen_w // 2, self.screen_h//2 - 100, 120, 50, "Succès", self.show_achievements)
        self.back_button = Button(85, 50, 120, 50, "Retour", self.show_main_menu)
        self.shop_button = Button(self.screen_w //2, self.screen_h // 2-10, 120,50, "Shop", self.show_shop_menu)

    def drawMenu(self):
        global previous_score
        background(125)
        if self.state == "main menu":
            self.draw_main_menu()
        elif self.state == "achievements":
            self.draw_achievements_menu()
        elif self.state == "in game":
            finished,previous_score = draw_game()
            if finished:
                self.state = "main menu"
        elif self.state == "shop":
            self.draw_boutique()

    def draw_main_menu(self):
        self.start_button.draw()
        self.achievements_button.draw()
        self.shop_button.draw()
        self.draw_credit()
        d = BDD_IMPORT.get_rows()[0][1]
        text_align(CORNER)
        text("Best Score: "+str(d),10,10)
        text("Previous Score: "+str(previous_score), 10,30)

    def draw_credit(self):
        rectMode(CORNER)
        fill(75)
        rect(0,self.screen_h*0.9,self.screen_w,self.screen_h*0.1)
        text_size(15)
        text_align(CENTER, CENTER)
        fill(0)
        text("Made by Sam, Alex & Isaac",self.screen_w//2, self.screen_h*0.95)

    def draw_achievements_menu(self):
        fill(255)
        rectMode(CORNER)
        rect(20, 20, self.screen_w - 40, self.screen_h - 40)
        fill(0)
        text_size(30)
        text("Succès Débloqués", (self.screen_w // 2, 60))

        y = 120
        self.collect_buttons = []
        for achievement in self.achievements:
            achievement.draw_achievement(200, y)
            if achievement.completed and not achievement.collected:
                btn = Button(560, y+25, 110, 40, "Collect", achievement.collect_reward)
                self.collect_buttons.append(btn)
                btn.draw()
            y += 80

        self.back_button.draw()

    def draw_boutique(self):
        fill(255)
        rectMode(CORNER)
        rect(20, 20, self.screen_w - 40, self.screen_h - 40)
        fill(0)
        text_size(30)
        text("Shop", (self.screen_w // 2, 60))
        self.back_button.draw()

    def show_achievements(self):
        self.state = "achievements"

    def show_main_menu(self):
        self.state = "main menu"

    def show_shop_menu(self):
        self.state = "shop"

    def mPressed(self):
        if self.state == "main menu":
            if self.start_button.is_hovered(mouse_x, mouse_y) and getMousePressed(): #type: ignore
                self.state="in game"
                print("Start button pressed!")
                setupGame()
            elif self.achievements_button.is_hovered(mouse_x, mouse_y) and getMousePressed(): #type: ignore
                self.show_achievements()
            elif self.shop_button.is_hovered(mouse_x, mouse_y) and getMousePressed(): #type: ignore
                self.show_shop_menu()
        elif self.state == "achievements":
            if self.back_button.is_hovered(mouse_x, mouse_y) and getMousePressed(): #type: ignore
                self.show_main_menu()
            for btn in self.collect_buttons:
                if btn.is_hovered(mouse_x, mouse_y) and getMousePressed(): #type: ignore
                    btn.click()