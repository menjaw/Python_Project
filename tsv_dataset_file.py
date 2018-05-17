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
    """Question 4 - When was 'Tuna - canned' most expensive?"""
    frame = pd. DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    expensive = tuna.sort_values(by="Price", ascending=False).head(1)
    return expensive


def most_cheapest_product():
    """Question 5 - Show the most cheapest product"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    cheapest = frame.sort_values(by='Price', ascending=True).head(1)
    return cheapest


def most_expensive_product():
    """Question 6 - Show the most expensive product"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    expensive = frame.sort_values(by='Price', ascending=False).head(1)
    return expensive


def top_10_cheapest_products():
    """Question 7 - Show the top 10 cheapest food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(by='Price', ascending=True).drop_duplicates(subset='Product').head(10)
    return filtered_frame


def top_10_most_expensive_products():
    """Question 8 - Show the top 10 most expensive food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(by='Price', ascending=False).drop_duplicates('Product').head(10)
    return filtered_frame


def average_price_bananas_2012():
    """Question 9 - What was the average price for 1 kg bananas in 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (df.Period >= 2012.01) & (df.Period < 2013.01)]
    average = banana['Price'].mean()
    return average


def average_price_bananas_2013():
    """Question 10 - What was the average price for 1 kg bananas in 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)]
    average = banana['Price'].mean()
    return average


def price_for_carrots_march_2012():
    """Question 11 - What was the price for 1 kg carrots in marts 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(df.Series_title_1 == "Carrots, 1kg") & (df.Period == 2012.03)]
    return carrot


def price_for_carrots_march_2013():
    """Question 12 - What was the price for 1 kg carrots in marts 2013?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(df.Series_title_1 == "Carrots, 1kg") & (df.Period == 2013.03)]
    return carrot


"""RUN THE METHODS"""
print("The total amount that have been tested is {} products".format(total_products_investigated()))
print(single_product_investigated())
print(year_of_cheapest_tuna())
print(year_of_most_expensive_tuna())
print(most_cheapest_product())
print(most_expensive_product())
print(top_10_cheapest_products())
print(top_10_most_expensive_products())
print(average_price_bananas_2012())
print(average_price_bananas_2013())
print(price_for_carrots_march_2012())
print(price_for_carrots_march_2013())


"""
#---------------------------TEST OTHER POSSIBILITIES NOT IN USE---------------------------------------------
period = df['Series_reference'][0:10].str.split(',')
print(period)


#Choose specific columns
#columns = df[df.columns[1:3]][0:10]
#print(pd.DataFrame(columns))
"""
