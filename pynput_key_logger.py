from pynput.mouse import Controller as MouseController, Listener as MouseListener
from pynput.keyboard import Controller as KeyboardController, Listener as KeyboardListener
from key_codes import key_codes


def control_mouse():
    mouse = MouseController()
    mouse.position = (500, 200)


def control_keyboard():
    keyboard = KeyboardController()
    keyboard.type("Hello world!")


def write_mouse_movement(x, y):
    print("Position of current mouse: {}, {}".format(x, y))


def listen_mouse():
    with MouseListener(on_move=write_mouse_movement) as mouse_listener:
        mouse_listener.join()


def write_from_keyboard_to_file(key):
    letter = str(key).strip("'")
    if letter in key_codes.keys():
        letter = key_codes.get(letter)
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(letter)


def listen_keyboard():
    with KeyboardListener(on_press=write_from_keyboard_to_file) as keyboard_listener:
        keyboard_listener.join()


listen_keyboard()
