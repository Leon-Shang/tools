import re
import json
import os 
from .general import get_input_output_dir


def combine_lines():
    input_dir, output_dir = get_input_output_dir()


    with open(input_dir, 'r') as file:
        text = file.read()
        lines = text.split('\n')
        lines_iter = iter(lines)
        line_block = {
            'lines': [],
            'equation_pos': []
        }
        new_lines = []
        while True:
            try:
                line = next(lines_iter)
                if line != '': 
                    # check list of markdown
                    if line.startswith('#'):
                        line += '\n'
                        if len(line_block['lines']) > 0:
                            line = '\n' + line
                    elif re.match(r' *-',line):
                        line += '\n'
                    elif line.startswith('$$'):
                        line_block['equation_pos'].append(len(line_block['lines']))
                    elif line.endswith('.'):
                        line += ' '
                    line_block['lines'].append(line)
                else:
                    if line_block['equation_pos']:
                        for i in range(len(line_block['equation_pos'])//2):
                            start = line_block['equation_pos'][i*2]
                            end = line_block['equation_pos'][i*2+1]+1
                            line_block['lines'][start:end] = [_ + '\n' for _ in line_block['lines'][start:end]]
                            line_block['lines'][start] = '\n'+line_block['lines'][start]
                    new_lines.append(''.join(line_block['lines']))
                    line_block = {
                        'lines': [],
                        'equation_pos': []
                    }
            except StopIteration:
                break
        new_text = '\n'.join(new_lines)
            
    with open(output_dir, 'w') as file:
        file.write(new_text)
