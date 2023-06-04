import re
from .general import get_input_output_dir

input_dir, output_dir = get_input_output_dir(input_file='output.md')

def extract_references():
    reference_list = []
    reference_texts = ''
    with open(input_dir, 'r') as file:
        text = file.read()
        reference_iter=  re.finditer(r'\[.*?\]', text)
        while True:
            try:
                reference = next(reference_iter) 
                end_pos = reference.end()
                if text[end_pos] == '(':
                    continue
                else:
                    if reference not in reference_list:
                        reference_list.append(reference.group())
            except StopIteration:
                break
    
    for i, reference in enumerate(reference_list):
        text = text.replace(reference, f'[{i+1}]')
        reference_texts += f'{i+1}. {reference[1:-1]}\n'
    with open(output_dir, 'w') as file:
        file.write(text)
        file.write('\n# References\n')
        file.write(reference_texts)

