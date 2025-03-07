
W,H = 650,650
ScreenHypothenuse = (W**2 + H**2) ** .5
player_size = 20
player_color = (255,0,0)
canon_color = (0,0,0)
bullet_color = (255, 102, 13)

def getScreenSize() -> tuple[int,int]:
    """Retourne la taille de l'écran du jeu."""
    return (W,H)

def getScreenHypotenuse() -> float:
    """Retroune l'hypothénuse de l'écran. Utile pour savoir si quelque chose sort de l'écran."""
    return ScreenHypothenuse

def getPlayerSize() -> int:
    return player_size

def getPlayerColor() -> tuple[int,int,int]:
    return player_color

def getCanonColor() -> tuple[int,int,int]:
    return canon_color

def getBulletColor() -> tuple[int,int,int]:
    return bullet_color

def changePlayerColor(newColor:tuple[int:int:int]) -> tuple[int,int,int]:
    global player_color
    player_color=newColor
    return player_color

def changeCanonColor(newColor:tuple[int:int:int]) -> tuple[int,int,int]:
    global canon_color
    canon_color=newColor
    return canon_color

def changeBulletColor(newColor:tuple[int:int:int]) -> tuple[int,int,int]:
    global bullet_color
    bullet_color=newColor
    return bullet_color