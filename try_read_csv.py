import csv
import plotly.plotly as py
import plotly.graph_objs as go

with open('food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv', newline='') as fp:
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

# Bar Charts
# 1: NOT WORKING
bar_chart = [go.Bar(x=["Buh", "Bøh"], y=[2, 5])]
py.plot(bar_chart, filename='basic-bar')

# 2: NOT WORKING
data = [go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23]
    )]

py.iplot(data, filename='basic-bar')