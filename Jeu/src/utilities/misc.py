def clamp(x:float,min:float,max:float):
    """Encadre la valeur x entre min et max"""
    if x < min:
        x = min
    elif x > max:
        x = max
    return x