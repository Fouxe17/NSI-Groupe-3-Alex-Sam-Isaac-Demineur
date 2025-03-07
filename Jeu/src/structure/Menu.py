from p5 import *
from src.classes.GameMenu import *

def draw_menu(menu:GameMenu):
    menu.drawMenu()


def m_p(menu:GameMenu):
    if mouse_is_pressed: #type:ignore
        menu.mPressed()