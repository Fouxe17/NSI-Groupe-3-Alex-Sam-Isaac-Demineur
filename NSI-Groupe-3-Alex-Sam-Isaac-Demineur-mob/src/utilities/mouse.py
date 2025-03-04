clicking:bool = False
previous_click: bool = False

def getMousePosition() -> tuple[int,int]:
    """Obtiens la position de la souris à l'écran."""
    return (mouse_x,mouse_y) #type: ignore

def getMousePressed() -> bool:
    """Retourne un booléen pour savoir si la souris est appuyé (MouseButton1)"""
    return mouse_is_pressed #type: ignore

def onClickEvent() -> bool:
    """
    Renvoie si la souris a changé détat sur la frame actuelle
    ```
        appuyée = mouse.onClickEvent()
        if appuyée:
            print("J'ai cliqué avec la souris !")
    ```
    
    Si oui, alors la souris a été cliquée.
    """
    return clicking != previous_click and clicking

def getMousePressedInArea(x,y,sx,sy) -> bool:
    """Retourne si la souris est situé dans une boxe."""
    mx,my = getMousePosition()
    if not getMousePressed(): return False
    if mx > x - sx/2 and mx < x + sx/2:
        if my > y - sy/2 and my < y + sy/2:
            return True
    return False

def update():
    global clicking, previous_click
    previous_click = clicking
    clicking = getMousePressed()