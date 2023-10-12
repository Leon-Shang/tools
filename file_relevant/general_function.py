import os
import glob

def delete_all_files(folder_path, reserve_dir=[]):
    # Get a list of all files in the folder
    files = glob.glob(folder_path + '/*')
    for dir in reserve_dir:
        if f'{folder_path}/{dir}' in files:
            files.remove(dir)
    # Iterate through the list of files and delete each one
    for file in files:
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            delete_all_files(file)
            os.rmdir(file)


def get_all_file_dirs(folder_path):
    # Get a list of all files in the folder
    files = glob.glob(folder_path + '/*')
    file_dirs = []
    # Iterate through the list of files and delete each one
    for file in files:
        if os.path.isfile(file):
            file_dirs.append(file)
        elif os.path.isdir(file):
            file_dirs.extend(get_all_file_dirs(file))
    return file_dirs