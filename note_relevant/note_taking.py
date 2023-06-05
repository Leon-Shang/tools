# Take notes from clipboard
import pyperclip
import os
from pynput import keyboard

from string_relevant.md_type.string_to_list import text_to_md_list
from codes_relevant.recognize import recognize_programming_language



class Text2MdHead:
    def __init__(self, head_level):
        self.head_level = head_level

    def do(self, text):
        return '#' * self.head_level + ' ' + text

def text_to_md_code_block(text):
    language = recognize_programming_language(text)
    return f'```{language}\n{text}\n```'

def create_key_to_command():
    key_to_command = {}
    for i in range(1, 10):
        # right number key from 1 to 9, 1 is 97, 9 is 105
        key_to_command[96+i] = Text2MdHead(i).do
    key_to_command[106] = text_to_md_code_block
    key_to_command[107] = lambda text: '=='+text+'==' # + key
    key_to_command[109] = text_to_md_list # - key
    key_to_command[110] = lambda text: '`'+text+'`' # . key
    key_to_command[111] = lambda text: '\n'+text # / key
    return key_to_command


def transform_to_md_keyboard(text):
    key_to_command = create_key_to_command()
    def on_press(key):
        nonlocal text
        nonlocal listener
        if key == keyboard.Key.ctrl_l:
            listener.stop()
            
        if hasattr(key, 'vk'):
            if key.vk in key_to_command:
                text = key_to_command[key.vk](text)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        print('listener stop')
    return text
        
def write_to_md(text, note_dir):
    with open(note_dir, 'a', encoding='utf-8') as f:
        f.write(text + '\n')

def take_notes_from_clipboard(note_folder = r'note_relevant\note_folder',note_name = 'note.md'):
    
    note_dir = os.path.join(note_folder, note_name)
    os.makedirs(note_folder, exist_ok=True) 
    print('Taking notes from clipboard, press Ctrl+C to stop')
    try: 
        old_clip = ''
        while True:
            new_clip = pyperclip.waitForNewPaste()
            if new_clip in old_clip and new_clip != '':
                old_clip = old_clip.replace(new_clip, f'**{new_clip}**')
            else:
                if old_clip != '':
                    write_to_md(old_clip, note_dir)
                old_clip = transform_to_md_keyboard(new_clip)
    except KeyboardInterrupt:
        write_to_md(old_clip, note_dir)
if __name__ == '__main__':
    take_notes_from_clipboard(note_dir)
