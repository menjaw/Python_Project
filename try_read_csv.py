import csv

with open('food-price-index-mar18-weighted-average-prices-csv-tables.csv.csv', newline='') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    header_row = next(reader)
    for row in reader:
        print(row)
        if reader.line_num > 5:
            break





#Another example
with open('food-price-index-mar18-weighted-average-prices-csv-tables.csv.csv') as fp:
    lines = fp.readlines()

print(lines[0:5])
