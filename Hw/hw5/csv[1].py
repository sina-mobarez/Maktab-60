import csv

file_name = 'numcsv.csv'
headers = ('first', 'second', 'third')
data = [
    {'first': 1,
     'second': 2,
     'third': 3},
    {'first': 2,
     'second': 3,
     'third': 4},
    {'first': 5,
     'second': 6,
     'third': 7},
    {'first': 8,
     'second': 9,
     'third': 10}
]
out_file = 'swaped.csv'


# write a new csv file with above data
def write_csv(headers, data, filename):
    with open(filename, 'w+', newline='') as csvfile:
        numbers = csv.DictWriter(csvfile, fieldnames=headers)
        numbers.writeheader()
        numbers.writerows(data)


# this function swap columns in csv file
def swap_columns(in_file, out_file):
    with open(in_file, 'r') as infile, open(out_file, 'a') as outfile:
        fieldname = ['first', 'third', 'second']
        writer = csv.DictWriter(outfile, fieldnames=fieldname)
        writer.writeheader()
        for row in csv.DictReader(infile):
            writer.writerow(row)


# this function plus all rows in csv file and write it in fourth row
def plus_rows(in_file):
    with open(in_file, 'r') as infile:
        reader = csv.DictReader(infile)
        columns = []
        for i in reader:
            row = {
                'first': i['first'],
                'second': i['second'],
                'third': i['third'],
                'sum': int(['first']) + int(i['second']) + int(i['third'])
            }
            columns.append(row)
        with open(in_file, 'w+', newline='') as op:
            header = ['first', 'second', 'third', 'sum']
            writer = csv.DictWriter(op, fieldnames=header)
            writer.writerow(dict((heads, heads) for heads in header))
            writer.writerows(columns)


write_csv(headers, data, file_name)
swap_columns(file_name, out_file)
plus_rows(out_file)
print(type(data[0]["first"]))