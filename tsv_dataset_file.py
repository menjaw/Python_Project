import pandas as pd
import matplotlib as plt


df = pd.read_csv('food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv', sep='\t')


#Create dictonary with the wanted columns
data = {
    'ref': df['Series_reference'],
    'Period': df['Period'],
    'Price': df['Data_value'],
    'Product': df['Series_title_1'],
    'Amount': 0
    }


def total_products_investigated():
    """Question 1 - How many products have been testet?"""
    total_amount = len(df.drop_duplicates(['Series_title_1']))
    return total_amount


print(total_products_investigated())


def single_product_investigated():
    """Question 2 - How many times have each product been testet?"""

    # Put columns together
    amount = pd.DataFrame(data, columns=['Product', 'Amount'])

    result = amount.groupby(['Product']).count()
    return result


print(single_product_investigated())




"""
#---------------------------TEST OTHER POSSIBILITIES---------------------------------------------
period = df['Series_reference'][0:10].str.split(',')
print(period)


#Choose specific columns
#columns = df[df.columns[1:3]][0:10]
#print(pd.DataFrame(columns))
"""