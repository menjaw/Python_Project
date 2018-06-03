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


"""Question 1 - How many products have been tested?"""
# Should/could be answered with a pie chart
total_amount = len(df.drop_duplicates(['Series_title_1']))
print(total_amount)

"""Question 2 - How many times have each product been tested?"""
# Should/could be answered with a bar diagram.
# Depending on the result from question 1, should consider how many products will be shown.

"""Question 3 - When was 'Tuna - canned' cheapest?"""
# Should/could be answered with line chart diagram.

"""Question 4 - When was 'Tuna - canned' most expensive?"""
# Should probably join question 3 and 4 together with.

"""Question 5 - Show the most cheapest product"""
# Should refrase the question to be more specific in regards to date.

"""Question 6 - Show the most expensive product"""
# Could be done as a linechart or bardiagram

"""Question 7 - Show the top 10 cheapest food products"""
# Should/could be answered with a bar diagram.

"""Question 8 - Show the top 10 most expensive food products"""
# Should/could be answered with a bar diagram.

"""Question 9 - What was the average price for 1 kg bananas in 2012?"""
# Should/could be answered with line chart diagram.

"""Question 10 - What was the average price for 1 kg bananas in 2012?"""

"""Question 11 - What was the price for 1 kg carrots in marts 2012?"""
# I think this should maybe be refrased to get more out of the question.
# Could be a time period such as: from march 2012 - march 2018

"""Question 12 - What was the price for 1 kg carrots in marts 2013?"""
# Again i think, this could be refrased to provide more data than just a number.

"""In which period was 1 kg kiwi cheapest and what was the price? (Show top 10)"""
# Line chart

"""In which period was 1 kg kiwi most expensive and what was the price? (Show top 10)"""
# Just like Kiwi.
