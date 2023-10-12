import csv 
import os
import pandas as pd
# read csv to dict 

def read_csv_to_dict(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
    
def read_csv_to_df(csv_file):
    # UnicodeDecodeError: 'utf-8' codec can't decode bytes in position 42648-42649: invalid continuation byte
    return pd.read_csv(csv_file, encoding='ISO-8859-1')

def lower_all_alphabet_string(input_string):
    output_string = ''.join([c for c in input_string if c.isalpha()]).lower()
    # remove character like â
    output_string = ''.join([c for c in output_string if ord(c) < 128])
    return output_string

def get_title_without_years(title):
    return title.split('_')[0]


def get_df_from_dir(input_dir):
    files = os.listdir(input_dir)
    for file in files:
        if file.endswith('.csv'):
            input_csv_file = f'{input_dir}/{file}'
    csv_df = read_csv_to_df(input_csv_file)
    title_column_list = ['Title', 'Document Title', 'Article title']
    for column in csv_df.columns:
        if column in title_column_list:
            title_column = column
            break
    csv_df[title_column] = csv_df[title_column].apply(lower_all_alphabet_string)
    csv_df.set_index(title_column, inplace=True)
    return csv_df

def get_years_classification(csv_df, input_dir):
    years_classification = {}
    files = os.listdir(input_dir)
    year_column_list = ['Year', 'Publication Year', 'Volume year']
    for column in csv_df.columns:
        if column in year_column_list:
            year_column = column
            break
    for file in files:
        if file.endswith('.pdf'):
            title = file.split('.')[0]
            title_key = get_title_without_years(title)
            title_key = lower_all_alphabet_string(title_key)
            for title_in_df in csv_df.index:
                if title_key in title_in_df:
                    title_key = title_in_df
                    break
                
            the_row = csv_df.loc[title_key]
            year = the_row[year_column]
            if the_row[year_column] not in years_classification:
                years_classification[year] = []
            years_classification[year].append(title)
    return years_classification


def move_files_to_year_folder(years_classification, input_dir, journal_name):
    output_folder = '/'.join(input_dir.split('/')[:-2])
    for year in years_classification:
        paper_number_this_year = len(years_classification[year])
        new_folder = f'{output_folder}/Process_{journal_name}{year}_{paper_number_this_year}'
        os.makedirs(new_folder, exist_ok=True)
        for title in years_classification[year]:
            os.rename(f'{input_dir}/{title}.pdf', f'{new_folder}/{title}.pdf')



dir = 'files/csv/files_to_move'
folders = os.listdir(dir)
for folder in folders:
    input_dir = f'{dir}/{folder}'
    csv_df = get_df_from_dir(input_dir)
    years_classification = get_years_classification(csv_df, input_dir)
    move_files_to_year_folder(years_classification, input_dir, folder)


