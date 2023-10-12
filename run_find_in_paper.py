from file_relevant.general_function import  delete_all_files, get_all_file_dirs
from paper_relevance.find_in_paper import FindInPaper



find_in_paper = FindInPaper()


folder_dir = "paper_relevance/papers"
all_file_dirs = get_all_file_dirs(folder_dir)
for file in all_file_dirs:
    # print(file)
    text = find_in_paper.extract_text_pypdf2(file)
    # delete all symbols
    text_pure = ""
    for c in text:
        if c.isalnum():
            text_pure += c
    text = text_pure
    finding_target = '71771173'
    if find_in_paper.find(text, finding_target):
        print("Found in {}".format(file))
    else:
        print("Not found in {}".format(file))