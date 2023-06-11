from pynput import keyboard

def add_keyboard_listener_on_press(on_press: callable) -> None:

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        print('listener stop')