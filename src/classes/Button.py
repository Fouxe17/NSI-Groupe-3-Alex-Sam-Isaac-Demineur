from p5 import *

class Button:
    def __init__(self, x, y, width, height, text, callback=None):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.text = text
        self.callback = callback

    def draw(self):
        fill(224)
        rectMode(CENTER)
        rect(self.x, self.y, self.w, self.h)
        fill(0)
        text_align(CENTER, CENTER)
        text_size(20)
        text(self.text, self.x, self.y)

    def is_hovered(self, mx, my):
        return self.x - self.w//2 < mx < self.x + self.w//2 and self.y - self.h//2 < my < self.y + self.h//2

    def click(self):
        if self.callback:
            self.callback()