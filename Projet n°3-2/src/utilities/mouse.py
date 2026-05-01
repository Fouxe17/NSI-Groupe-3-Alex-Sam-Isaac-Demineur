def getMousePosition():
    """Obtiens la position de la souris à l'écran."""
    return (mouse_x,mouse_y) #type: ignore

def getMousePressed():
    """Retourne un booléen pour savoir si la souris est appuyé (MouseButton1)"""
    return mouse_is_pressed #type: ignore

def getMousePressedInArea(x,y,sx,sy) -> bool:
    """Retourne si la souris est situé dans une boxe."""
    mx,my = getMousePosition()
    if not getMousePressed(): return False
    if mx > x - sx/2 and mx < x + sx/2:
        if my > y - sy/2 and my < y + sy/2:
            return True
    return False