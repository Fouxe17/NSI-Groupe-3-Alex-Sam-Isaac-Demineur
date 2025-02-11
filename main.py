from p5 import *
from src.structure.Menu import *
from src.classes.GameMenu import *

from pathlib import Path

current_path = Path.cwd()

menu = GameMenu()
current_font = None

def setup():
    menu.setup()

def draw():
    global current_font
    if current_font == None:
        current_font = create_font("./fonts/LIBERATIONMONO-REGULAR.ttf")
    text_font(current_font)
    menu.drawMenu()
    m_p(menu)

run()
