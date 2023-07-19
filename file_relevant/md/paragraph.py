import re
import json
import os 
from .general import MdProcessor

class MdLineProcessor(MdProcessor):

    def check_lists(self, line, line_block):
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
    
    def add_equation(self, line_block):
        for i in range(len(line_block['equation_pos'])//2):
            start = line_block['equation_pos'][i*2]
            end = line_block['equation_pos'][i*2+1]+1
            line_block['lines'][start:end] = [_ + '\n' for _ in line_block['lines'][start:end]]
            line_block['lines'][start] = '\n'+line_block['lines'][start]

    def get_new_lines(self, lines_iter):
        line_block = {
            'lines': [],
            'equation_pos': []
        }
        new_lines = []
        while True:
            try:
                line = next(lines_iter)
                if line != '': 
                    self.check_lists(line, line_block)
                else:
                    if line_block['equation_pos']:
                        self.add_equation(line_block)
                    new_lines.append(''.join(line_block['lines']))
                    line_block = {
                        'lines': [],
                        'equation_pos': []
                    }
            except StopIteration:
                break

        return new_lines

    def combine_lines(self):
        input_dir = self.input_dir
        output_dir = self.output_dir

        with open(input_dir, 'r') as file:
            text = file.read()
            lines = text.split('\n')
            lines_iter = iter(lines)
            new_lines = self.get_new_lines(lines_iter)
            new_text = '\n'.join(new_lines)
                
        with open(output_dir, 'w') as file:
            file.write(new_text)
