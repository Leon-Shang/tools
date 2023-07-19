import nbformat as nbf
import csv
import os

class TxtTransform:
    
    def __init__(self) -> None:
        pass
    
    def transform_one_file(self, txt_file, new_file):
        # Read the .txt file
        with open(txt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            self.transform(lines, new_file)

    def run_from_folder(self):
        for f in os.listdir(self.folder_path):
            if f.endswith('.txt'):
                self.transform_one_file(f'{self.folder_path}/{f}', f'{self.folder_path}/{f.split(".")[0]}.{self.extension}')

class TxtToIpynb(TxtTransform):

    folder_path = 'files/txt_to_ipynb'
    extension = 'ipynb'

    def transform(self, lines, output_dir):
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
        with open(output_dir, 'w', encoding='utf-8') as f:
            nbf.write(nb, f)

class TxtToCsv(TxtTransform):

    folder_path = 'files/txt_to_csv'
    extension = 'csv'
    first_line = ['Author full names', 'Title', 'Source title', 'Volume', 'Year', 'Pages', 'ISSN', 'DOI', 'Link', 'Abstract', 'Keywords']
    def transform(self, lines, output_dir):
        all_rows = []
        separator_line = '\n'
        present_row = []
        for line in lines:
            if line == separator_line:
                all_rows.append(present_row)
                present_row = []
            else:
                present_row.append(line.strip(' ,\n'))
        if present_row != []: all_rows.append(present_row)
        # write all rows to csv
        with open(output_dir, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.first_line)
            for row in all_rows:
                writer.writerow(row)

if __name__ == '__main__':
    # TxtToIpynb().run_from_folder()
    TxtToCsv().run_from_folder()
