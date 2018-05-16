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
    frame = pd.DataFrame(data, columns=['Product', 'Amount'])

    amount = frame.groupby(['Product']).count()
    return amount


def year_of_cheapest_tuna():
    """Question 3 - When was 'Tuna - canned' cheapest?"""
    frame = pd. DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    cheapest = tuna.sort_values(by="Price").head(1)
    return cheapest


def year_of_most_expensive_tuna():
    """Question 4 - When was 'Tuna - canned' cheapest?"""
    frame = pd. DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    expensive = tuna.sort_values(by="Price", ascending=False).head(1)
    return expensive


def most_cheapest_product():
    """Question 5 - Show the most cheapest product"""
    frame = pd.DataFrame(data, columns=['Product', 'Price'])
    cheapest = frame.sort_values(by='Price', ascending=True).head(1)
    return cheapest


def most_expensive_product():
    """Question 6 - Show the most cheapest product"""
    frame = pd.DataFrame(data, columns=['Product', 'Price'])
    expensive = frame.sort_values(by='Price', ascending=False).head(1)
    return expensive


def top_10_cheapest_products():
    """Question 7 - Show the top 10 cheapest food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price'])
    filtered_frame = frame.drop_duplicates('Product').nsmallest(10, 'Price')
    return filtered_frame


def top_10_most_expensive_products():
    """Question 8 - Show the top 10 most expensive food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price'])
    filtered_frame = frame.drop_duplicates('Product').nlargest(10, 'Price')
    return filtered_frame


"""RUN THE METHODS"""
print("The total amount that have been tested is {} products".format(total_products_investigated()))
#print(single_product_investigated())
print(year_of_cheapest_tuna())
print(year_of_most_expensive_tuna())
print(most_cheapest_product())
print(most_expensive_product())
print(top_10_cheapest_products())
print(top_10_most_expensive_products())





"""
#---------------------------TEST OTHER POSSIBILITIES NOT IN USE---------------------------------------------
period = df['Series_reference'][0:10].str.split(',')
print(period)


#Choose specific columns
#columns = df[df.columns[1:3]][0:10]
#print(pd.DataFrame(columns))
"""
