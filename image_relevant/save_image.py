from PIL import ImageGrab
import datetime
import os 
def save_image_from_clipboard(name=None, if_time_stamp=True, image_type='png', save_folder='.'):
    try:
        if name is None:
            name = 'undefined'
        if if_time_stamp:
            name = name + '_' +datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f'{name}.{image_type}'
        save_dir = os.path.join(save_folder, file_name)
        os.makedirs(save_folder, exist_ok=True)
        ImageGrab.grabclipboard().save(save_dir, image_type.upper())
        print(f'Image saved to {save_dir}')
        return file_name
    except:
        print('No image in clipboard')
        return None

if __name__ == '__main__':
    save_image_from_clipboard()