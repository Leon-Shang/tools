import nbformat as nbf
import os
folder_path = 'files/txt_to_ipynb'
def txt_to_ipynb(txt_file, ipynb_file):
    # Read the .txt file
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Create a new notebook
    nb = nbf.v4.new_notebook()

    # Iterate over the lines in pairs and add them to the notebook
    for i in range(0, len(lines), 2):
        # Take two lines at a time
        text = lines[i:i+2]
        # Convert list of lines to a single string
        text = '\n综述：'.join(text)
        text += '\n模型图：\n\n案例数据'
        # Create a new markdown cell
        cell = nbf.v4.new_markdown_cell(text)
        # Add the cell to the notebook
        nb['cells'].append(cell)

    # Write the notebook to a .ipynb file
    with open(ipynb_file, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

# Example usage
for f in os.listdir(folder_path):
    if f.endswith('.txt'):
        txt_to_ipynb(f'{folder_path}/{f}', f'{folder_path}/{f.split(".")[0]}.ipynb')
