from p5 import *
from src.utilities.mouse import *

class Button:
    def __init__(self, x, y, width, height, text=None, callback=None,color=(224,224,224),callback2=None):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.text = text
        self.callback = callback
        self.color = color
        self.callback2 = callback2

    def draw(self):
        fill(*self.color)
        rectMode(CENTER)
        rect(self.x, self.y, self.w, self.h)
        if not self.text == None:
            fill(0)
            text_align(CENTER, CENTER)
            text_size(20)
            text(self.text, self.x, self.y)

    def is_hovered(self, mx, my):
        return self.x - self.w//2 < mx < self.x + self.w//2 and self.y - self.h//2 < my < self.y + self.h//2

    def click(self):
        if self.callback:
            self.callback()
        if self.callback2:
            self.callback2()
