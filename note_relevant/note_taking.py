# Take notes from clipboard
import pyperclip
import os
note_folder = r'note_relevant\note_folder'
note_name = 'note.md'
note_dir = os.path.join(note_folder, note_name)
os.makedirs(note_folder, exist_ok=True)


def take_notes_from_clipboard(note_dir):
    try: 
        old_clip = ''
        while True:
            new_clip = pyperclip.waitForNewPaste()
            if new_clip in old_clip:
                old_clip = old_clip.replace(new_clip, f'**{new_clip}**')
            else:
                if old_clip == '':
                    old_clip = new_clip
                    continue
                with open(note_dir, 'a') as f:
                    f.write(old_clip + '\n')
                    f.write('\n---\n')
                old_clip = new_clip
    except KeyboardInterrupt:
        with open(note_dir, 'a') as f:
            f.write(old_clip + '\n')
            f.write('\n---\n')
if __name__ == '__main__':
    take_notes_from_clipboard(note_dir)
