import os
import pandas as pd


df = pd.read_csv('food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv', sep='\t')

data = {
    'ref': df['Series_reference'],
    'Period': df['Period'],
    'Price': df['Data_value'],
    'Product': df['Series_title_1'],
    'Amount': 0
}

frame = pd.DataFrame(data, columns=['Price', 'Period'])
tuna = frame[df.Series_title_1 == "Oranges, 1kg"]
print(tuna['Price'].iloc[0])
