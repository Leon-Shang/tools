import json
import os

def add_citation():

    citation = "Your citation text here."


    input_folder = 'files/ipynb'
    for file in os.listdir(input_folder):
        with open(f'{input_folder}/{file}', 'r') as f:
            notebook = json.load(f)
        # Iterate through the cells and add a citation to each markdown cell
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown':
                source = cell['source']
                if not any(line.startswith('#') for line in source) and not any('citation' in line for line in source):
                    # Add citation at the end of the markdown cell
                    new_source = [].append(source)
                    cell['source'].insert(0, f'> {citation}\n\n')

        # Save the updated ipynb file
        with open(f'{input_folder}/updated_{file}', 'w') as f:
            json.dump(notebook, f, indent=1)
    from general_function import delete_all_files
    delete_all_files(input_folder)