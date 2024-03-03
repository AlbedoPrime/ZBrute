import keyboard

def print_char(event):
    if event.event_type == keyboard.KEY_DOWN:
        char = event.name
        if char.isprintable():
            print(char, end='')

keyboard.on_press(print_char)
keyboard.wait()