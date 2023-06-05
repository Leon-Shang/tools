# get import strings from clipboard
import pyperclip
import re
import re

def delete_comments(code):
    # delete single line comments
    code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)

    # delete multiline comments
    code = re.sub(r"'''[\s\S]*?'''", '', code)
    code = re.sub(r'"""[\s\S]*?"""', '', code)
    code = re.sub(r'\n\s*\n', '\n\n', code)
    return code


def delete_repetitive_import():

    import_strings = pyperclip.paste()
    import_strings = import_strings.split('\n')
    import_strings = [x.strip('\r') for x in import_strings]
    unique_import_strings = list(set(import_strings))
    # eleminate empty strings
    unique_import_strings = [x for x in unique_import_strings if x != '' and x != '\r']

    unique_import_strings.sort()
    unique_import_strings = '\n'.join(unique_import_strings)
    pyperclip.copy(unique_import_strings)
    print(unique_import_strings)

