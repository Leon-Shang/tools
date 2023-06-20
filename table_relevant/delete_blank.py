import csv 

## delete blank lines

def read_csv(input_file):
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        lines = [line for line in reader]
    return lines


def write_csv(output_file, lines):
    with open(output_file, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for line in lines:
            writer.writerow(line)

def delete_blank_lines(input_file, output_file):
    lines = read_csv(input_file)
    lines = [line for line in lines if line != []]
    write_csv(output_file, lines)

if __name__ == '__main__':
    delete_blank_lines('table_relevant/result.csv', 'table_relevant/result_new.csv')