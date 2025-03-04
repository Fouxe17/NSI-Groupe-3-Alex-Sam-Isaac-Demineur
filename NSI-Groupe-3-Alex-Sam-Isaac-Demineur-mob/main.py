from p5 import *
from src.structure.Menu import *
from src.classes.GameMenu import *
import pathlib

current_path = pathlib.Path.cwd()

font_path = current_path / "fonts" / "LIBERATIONMONO-REGULAR.ttf"
menu = GameMenu()
current_font = None

def setup():
    menu.setup()

def draw():
    global current_font
    if current_font == None:
        current_font = create_font(font_path)
    text_font(current_font)
    menu.drawMenu()
    m_p(menu)

run()