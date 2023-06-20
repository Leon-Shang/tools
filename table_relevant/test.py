import csv

def read_csv(input_file):
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        lines = [line for line in reader]
    return lines

lines = read_csv('table_relevant/result.csv')
lines = [line for line in lines if line != []]
print(lines)