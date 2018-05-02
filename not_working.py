import pandas as pd


df = pd.read_csv('food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv', sep='\t')


#Create dataframe with the wanted columns
data = {
    'ref': df['Series_reference'],
    'Period': df['Period'],
    'Price': df['Data_value'],
    'Product': df['Series_title_1']
    }

#Put columns together
result = pd.DataFrame(data, columns=['ref', 'Period', 'Price', 'Product'])[0:10]
print(result)

"""




#---------------------------TEST OTHER POSSIBILITIES---------------------------------------------
period = df['Series_reference'][0:10].str.split(',')
print(period)


#Choose specific columns
#columns = df[df.columns[1:3]][0:10]
#print(pd.DataFrame(columns))
"""