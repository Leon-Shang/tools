import os 


def change_md_name(target_name, folder_name='note_relevant/note_folder', origin_name='note'):
    input_dir = os.path.join(folder_name, origin_name+'.md')
    output_dir = os.path.join(folder_name, target_name+'.md')
    with open(input_dir, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.replace(origin_name+'.MarkdownAssets', target_name+'.MarkdownAssets')
    with open(output_dir, 'w', encoding='utf-8') as f:
        f.write(text)
    # change folder name 
    os.rename(os.path.join(folder_name, origin_name+'.MarkdownAssets'), os.path.join(folder_name, target_name+'.MarkdownAssets'))