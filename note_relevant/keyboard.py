from pynput import keyboard

def on_press(key):
    print(key)
    # print(key.char)
    print(key.vk)
    # if key.vk == 97: 
    #     print('a')
    print(type(key))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()