import os
import json


class MdProcessor:
    _folder_map_dir = 'files/folder_dir.json'
    input_file ='input.md'
    output_file = 'output.md'

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__dict__:
                self.__dict__[key] = value

        self.input_dir, self.output_dir = self.get_input_output_dir()


    def get_input_output_dir(self):
        with open(self._folder_map_dir, 'r') as file:
            folder_dir = json.load(file)

        input_md_dir = os.path.join(folder_dir['md'], self.input_file)
        output_md_dir = os.path.join(folder_dir['md'],self.output_file)
        return input_md_dir, output_md_dir   


def get_input_output_dir(input_file='input.md', output_file= 'output.md'):
    with open('files/folder_dir.json', 'r') as file:
        folder_dir = json.load(file)

    input_md_dir = os.path.join(folder_dir['md'], input_file)
    output_md_dir = os.path.join(folder_dir['md'],output_file)
    return input_md_dir, output_md_dir