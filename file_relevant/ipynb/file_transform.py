
import nbformat

with open('files/ipynb_to_md/interpretability.ipynb') as f:
    nb = nbformat.read(f, as_version=4)

from nbconvert import MarkdownExporter

exporter = MarkdownExporter()
output, resources = exporter.from_notebook_node(nb)

from general_function import delete_all_files
# Usage
folder_path = 'files/ipynb_to_md/'
delete_all_files(folder_path)