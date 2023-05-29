import pyperclip



def to_markdown_list_clipboard():
    """list-1

list-2
"""
    run_times = 0
    while True:
        run_times += 1
        print("The program has run {} times. Please press ctrl + c to terminate.".format(run_times))
        text = pyperclip.waitForNewPaste()
        lines = text.split('\n')
        # Remove blank lines
        lines = [line for line in lines if line.strip() != '']
        # Convert to markdown list
        md_list = '\n'.join('- ' + line for line in lines)
        pyperclip.copy(md_list)

# example usage

if __name__ == '__main__':
    to_markdown_list_clipboard()
