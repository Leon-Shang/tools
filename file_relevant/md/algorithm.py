from .general import get_input_output_dir
import re
input_dir, output_dir = get_input_output_dir(input_file='output.md')

def turn_algorithm_to_table():
    with open(input_dir, 'r') as file:
        text = file.read()
        lines = text.split('\n')
        lines_iter = iter(lines)
        line_block = {
            'lines': [],
            'equation_pos': []
        }
        algorithm_level = {}
        algorithm_index = {}
        line_number = 0
        while True:
            try:
                line = next(lines_iter)
                line_number += 1
                list_match = re.match(r' *- ', line)
                if list_match:
                    content = line[list_match.end()+1:]
                    if content.lower().startswith('algorithm'):
                        algorithm_level[content] = list_match.start()
                        algorithm_index[line_number] = content
            except StopIteration:
                break
    
    level_indent_map = {}
    indents = sorted(list(set(algorithm_level.values())))
    for i, indent in enumerate(indents):
        level_indent_map[indent] = i+1
    level_number = max(level_indent_map.values())
    for key, value in algorithm_index.items():
        table_row = [''] * level_number
        text[key-1] = f'{level_indent_map[algorithm_level[value]]}. {value}'
    with open(output_dir, 'w') as file:
        file.write(new_text)