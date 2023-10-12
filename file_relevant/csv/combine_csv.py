import os
import pandas as pd

def extract_title_year_journal():
    folder = 'files/csv/combine_csv'
    year_column_list = ['Year', 'Publication Year', 'Volume year']
    title_column_list = ['Title', 'Document Title', 'Article title']
    output_lines = []
    for main, subdirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.csv'):
                journal = main.split('\\')[-1]
                with open(os.path.join(main, file), 'r', encoding='ISO-8859-1') as f:
                    paper_table = pd.read_csv(f, encoding='ISO-8859-1')
                    for column in paper_table.columns:
                        if column in year_column_list:
                            year_column = column
                        if column in title_column_list:
                            title_column = column
                    for i in range(paper_table.shape[0]):
                        output_lines.append([paper_table[title_column][i], paper_table[year_column][i], journal])

    print(output_lines)
    with open(os.path.join(folder, 'title_year_journal.csv'), 'w', encoding='utf-8') as f:
        first_line = 'title,year,journal\n'
        f.write(first_line)
        for line in output_lines:
            f.write(f'"{line[0]}",{line[1]},{line[2]}\n')


extract_title_year_journal()