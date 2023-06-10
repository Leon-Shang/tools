# NOTICE: make sure the picture could be shown in the md file
import os
import re
import base64
import nbformat as nbf
from pathlib import Path
import requests
# Replace 'my_note_database.md' with the path to your markdown file

def transform_md_to_ipynb(file_name, folder_name= 'files/md_to_ipynb',transform_link = True):
    markdown_file_dir = f'{folder_name}/{file_name}.md'
    # Replace 'output_notebook.ipynb' with the desired output file name
    output_notebook = f'.ipynb'
    # Run the jupytext command
    os.system(f'jupytext --to {output_notebook} {markdown_file_dir}')

    def transform_link_to_attachment(folder_name, file_name):
        input_dir = f'{folder_name}/{file_name}.ipynb'
        output_dir =  f'{folder_name}/{file_name}_attach.ipynb'
        # Load the existing notebook
        with open(input_dir, "r") as f:
            nb = nbf.read(f, as_version=4)

        # Regular expression to match image links
        image_pattern = re.compile(r'!\[.*?\]\((.+?)\)')

        # Iterate through cells in the notebook
        new_cells = []
        for cell in nb.cells:
            if cell.cell_type == "markdown":
                # Search for image links in the Markdown cell
                matches = list(image_pattern.finditer(cell.source))
                if matches:
                    last_end = 0
                    for match in matches:
                        # Add the content before the image as a separate Markdown cell
                        content_before_image = cell.source[last_end:match.start()]
                        if content_before_image.strip():
                            new_cells.append(nbf.v4.new_markdown_cell(content_before_image))

                        image_path = match.group(1)
                        image_name = Path(image_path).name
                        image_name = "".join(char if char.isalnum() else "_" for char in image_name)
                        if image_path.endswith('.svg'):
                            if image_path.startswith("http"):
                                response = requests.get(image_path)
                                svg_data = response.content
                            else:
                                with open(f'{folder_name}/{image_path}', "r") as img_file:
                                    svg_data = img_file.read()
                            svg_base64 = base64.b64encode(svg_data.encode("utf-8")).decode("utf-8")
                            attachment_cell = nbf.v4.new_markdown_cell()
                            attachment_cell.source = f"![{image_name}](attachment:{image_name})"
                            attachment_cell.attachments = {
                                image_name: {
                                    "image/svg+xml": svg_base64
                                }   
                            }
                        else:
                        # Create a new Markdown cell with the image as an attachment
                            if image_path.startswith("http"):
                                # Download image from the URL
                                response = requests.get(image_path)
                                img_data = response.content

                                # Read image file

                            else:
                                with open(f'{folder_name}/{image_path}', "rb") as img_file:
                                    img_data = img_file.read()

                            img_base64 = base64.b64encode(img_data).decode("utf-8")
                            img_mime = f"image/{Path(image_path).suffix[1:]}"
                            attachment_cell = nbf.v4.new_markdown_cell()
                            attachment_cell.source = f"![{image_name}](attachment:{image_name})"
                            attachment_cell.attachments = {
                                image_name: {
                                    img_mime: img_base64
                                }
                            }
                        new_cells.append(attachment_cell)
                        last_end = match.end()

                    # Add the content after the last image as a separate Markdown cell
                    content_after_image = cell.source[last_end:]
                    if content_after_image.strip():
                        new_cells.append(nbf.v4.new_markdown_cell(content_after_image))
                else:
                    new_cells.append(cell)
            else:
                new_cells.append(cell)

        nb.cells = new_cells

        # Save the modified notebook
        with open(output_dir, "w") as f:
            nbf.write(nb, f)

    if transform_link:
        transform_link_to_attachment(folder_name, file_name)
folder_path = 'files/md_to_ipynb'
for file in os.listdir(folder_path):
    if file.endswith('.md'):
        transform_md_to_ipynb(file.split('.')[0])
from general_function import delete_all_files
# Usage

delete_all_files(folder_path, reserve_dir=['typora-user-images'])