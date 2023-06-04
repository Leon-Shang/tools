import os
import json

def get_input_output_dir(input_file='input.md', output_file= 'output.md'):
    with open('files/folder_dir.json', 'r') as file:
        folder_dir = json.load(file)

    input_md_dir = os.path.join(folder_dir['md'], input_file)
    output_md_dir = os.path.join(folder_dir['md'],output_file)
    return input_md_dir, output_md_dir