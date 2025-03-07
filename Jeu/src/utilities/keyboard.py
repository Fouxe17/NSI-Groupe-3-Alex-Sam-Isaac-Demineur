import keyboard
import threading

pressed_keys=[]

def key_listener():
    global pressed_keys
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if not event.name in pressed_keys:
                pressed_keys.append(event.name)
        elif event.event_type == keyboard.KEY_UP:
            key_position = False
            try:
                key_position = pressed_keys.index(event.name)
                pressed_keys.pop(key_position)
            except ValueError:
                print("Value not in list. Resetting pressed keys for recovery")
                pressed_keys = []

def getPressedKeys()->tuple[str]:
    """Retourne les clés du claviers qui sont appuyées."""
    return pressed_keys

listener_thread = threading.Thread(target=key_listener, daemon=True)
listener_thread.start()