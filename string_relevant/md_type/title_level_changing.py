import re
import pyperclip
from keyboard.add_listener import add_keyboard_listener_on_press


def change_title_level(text, level_diff=1, upgrade=True):
    adjusted_lines = []
    for line in text.split('\n'):
        match = re.match(r'^(#+)\s+(.*)$', line)
        if match:
            current_level = len(match.group(1))
            if upgrade:
                new_level = max(1, current_level - level_diff)
            else:
                new_level = min(6, current_level + level_diff)
            adjusted_lines.append(f"{'#' * new_level} {match.group(2)}")
        else:
            adjusted_lines.append(line)
    return '\n'.join(adjusted_lines)


def on_press(key):
    if hasattr(key, 'vk'):
        if key.vk == 107: # key +
            print('increase title level')
            text = pyperclip.paste()
            text = change_title_level(text, level_diff=1, upgrade=True)
            pyperclip.copy(text)
        if key.vk == 109: # key -
            print('decrease title level')
            text = pyperclip.paste()
            text = change_title_level(text, level_diff=1, upgrade=False)
            pyperclip.copy(text)


def title_level_changing():
    print('title_level_changing')
    add_keyboard_listener_on_press(on_press)
