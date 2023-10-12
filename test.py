import pyautogui 

for i in range(5):
    print(pyautogui.position())
    current_position = pyautogui.position()
    pyautogui.moveTo(500, 300, duration=0.25)
    pyautogui.moveTo(current_position)
    pyautogui.scroll(-200)

