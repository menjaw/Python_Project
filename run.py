import pandas as pd

#Read the file
df = pd.read_csv('food-price-index-mar18-index-numbers-csv-tables.csv.csv')


#Creates global dataframe with the wanted columns (dictinary)
data = {
    'Category': df['Series_title_1'],
    'Amount': 0,
    'Prices': df['Data_value'],
    'Period': df['Period']

}

#Methods
def category_amount_investigated():
    """Question 1 - How many times have each category been investigated?"""

    # Put columns together
    amount = pd.DataFrame(data, columns=['Category', 'Amount'])

    result = amount.groupby(['Category']).count()
    return result


def total_price_for_each_category():
    """What is the sum of all prices per category?"""
    price = pd.DataFrame(data, columns=['Category', 'Prices'])

    result = price.groupby(['Category']).mean()
    return result


def group_product_by_year():
    """For what years have the fruit and vegetables been tested?"""
    period = pd.DataFrame(data, columns=['Category', 'Period'])[0:10]
    result = df.loc[df['Series_title_1'] == 'Fruit and vegetables']
    return result


print(pd.__version__)


"""------RUN METHODS------"""
print(category_amount_investigated())
print(total_price_for_each_category())
#print(group_product_by_year())
