import re
import json
import os 


def find_latex_blocks(text):
    # Find all occurrences of '$$' in the text
    matches = re.findall(r'\$\$(.*?)\$\$', text, flags=re.DOTALL)
    matches_set = set(matches)
    return matches_set

def convert():

    with open('files/folder_dir.json', 'r') as file:
        folder_dir = json.load(file)

    input_md_dir = os.path.join(folder_dir['md'], 'input.md')
    output_md_dir = os.path.join(folder_dir['md'], 'output.md')



    def convert_multiline_latex_blocks(text):
        # Replace all occurrences of '\\\n' within '$$' blocks with '$$\n$$'
        return re.sub(r'\\\\', '\n'+r'$$'+'\n'+"$$", text)


    with open(input_md_dir, 'r') as file:
        text = file.read()
        latex_blocks_set = find_latex_blocks(text)
        for block in latex_blocks_set:
            new_block = convert_multiline_latex_blocks(block)
            text = text.replace(block, new_block)

    with open(output_md_dir, 'w') as file:
        file.write(text)

