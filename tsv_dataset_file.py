import pandas as pd


df = pd.read_csv('food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv', sep='\t')

# Create dictionary with the wanted columns
data = {
    'ref': df['Series_reference'],
    'Period': df['Period'],
    'Price': df['Data_value'],
    'Product': df['Series_title_1'],
    'Amount': 0
}


def total_products_investigated():
    """Question 1 - How many products have been tested?"""
    total_amount = len(df.drop_duplicates(['Series_title_1']))
    return total_amount


def single_product_investigated():
    """Question 2 - How many times have each product been tested?"""

    # Put columns together
    amount = pd.DataFrame(data, columns=['Product', 'Amount'])

    result = amount.groupby(['Product']).count()
    return result


def year_of_cheapest_tuna():
    """Question 3 - When was 'Tuna - canned' cheapest?"""
    frame = pd. DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    lowest = tuna.sort_values(by="Price").head(1)
    return lowest



"""RUN THE METHODS"""
print("The total amount that have been tested is {} products".format(total_products_investigated()))
print(year_of_cheapest_tuna())





"""
#---------------------------TEST OTHER POSSIBILITIES---------------------------------------------
period = df['Series_reference'][0:10].str.split(',')
print(period)


#Choose specific columns
#columns = df[df.columns[1:3]][0:10]
#print(pd.DataFrame(columns))
"""
