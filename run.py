import pandas as pd
import browser_view as bv
import line_chart_plot as lcp
import pygal

df = pd.read_csv('food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv', sep='\t')

# Initilize program from App
bv.initialize()


# Create dictionary with the wanted columns
data = {
    'ref': df['Series_reference'],
    'Period': df['Period'],
    'Price': df['Data_value'],
    'Product': df['Series_title_1'],
    'Amount': 0
}

frame = pd.DataFrame(data, columns=['Price', 'Period'])
tomatoes = frame[df.Series_title_1 == "Tomatoes, 1kg"]
cabbage = frame[df.Series_title_1 == "Cabbage, 1kg"]
lettuce = frame[df.Series_title_1 == "Lettuce, 1kg"]
oranges = frame[df.Series_title_1 == "Oranges, 1kg"]


@bv.app.route('/')
def show_data():
    return bv.render_template('index.html', data=df.to_html())


@bv.app.route('/1')
def total_products_investigated():
    """Question 1 - How many products have been tested?"""
    total_amount = len(df.drop_duplicates(['Series_title_1']))
    return bv.render_template('index.html', data=total_amount.to_html())


@bv.app.route('/2')
def single_product_investigated():
    """Question 2 - How many times have each product been tested?"""
    # Put columns together
    frame = pd.DataFrame(data, columns=['Product', 'Amount'])

    amount = frame.groupby(['Product']).count()
    return bv.render_template('index.html', data=amount.to_html())


@bv.app.route('/3')
def year_of_cheapest_tuna():
    """Question 3 - When was 'Tuna - canned' cheapest?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    cheapest = tuna.sort_values(by="Price").head(1)
    return bv.render_template('index.html', data=cheapest.to_html())


@bv.app.route('/4')
def year_of_most_expensive_tuna():
    """Question 4 - When was 'Tuna - canned' most expensive?"""
    frame = pd. DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    expensive = tuna.sort_values(by="Price", ascending=False).head(1)
    return bv.render_template('index.html', data=expensive.to_html())


@bv.app.route('/5')
def most_cheapest_product():
    """Question 5 - Show the most cheapest product"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    cheapest = frame.sort_values(by='Price', ascending=True).head(1)
    return bv.render_template('index.html', data=cheapest.to_html())


@bv.app.route('/6')
def most_expensive_product():
    """Question 6 - Show the most expensive product"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    expensive = frame.sort_values(by='Price', ascending=False).head(1)
    return bv.render_template('index.html', data=expensive.to_html())


@bv.app.route('/7')
def top_10_cheapest_products():
    """Question 7 - Show the top 10 cheapest food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(
        by='Price', ascending=True).drop_duplicates(subset='Product').head(10)
    return bv.render_template('index.html', data=filtered_frame.to_html())


@bv.app.route('/8')
def top_10_most_expensive_products():
    """Question 8 - Show the top 10 most expensive food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(
        by='Price', ascending=False).drop_duplicates('Product').head(10)
    return bv.render_template('index.html', data=filtered_frame.to_html())


@bv.app.route('/9')
def average_price_bananas_2012():
    """Question 9 - What was the average price for 1 kg bananas in 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (
        df.Period >= 2012.01) & (df.Period < 2013.01)]
    average = banana['Price'].mean()
    return bv.render_template('index.html', data=average.to_html())


@bv.app.route('/10')
def average_price_bananas_2013():
    """Question 10 - What was the average price for 1 kg bananas in 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (
        df.Period >= 2013.01) & (df.Period < 2014.01)]
    average = banana['Price'].mean()
    return bv.render_template('index.html', data=average.to_html())


@bv.app.route('/11')
def price_for_carrots_march_2012():
    """Question 11 - What was the price for 1 kg carrots in marts 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(df.Series_title_1 == "Carrots, 1kg") & (df.Period == 2013.03)]
    return bv.render_template('index.html', data=carrot.to_html())


@bv.app.route('/12')
def price_for_carrots_march_2013():
    """Question 12 - What was the price for 1 kg carrots in marts 2013?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(df.Series_title_1 == "Carrots, 1kg") & (df.Period == 2013.03)]
    return bv.render_template('index.html', data=carrot.to_html())


@bv.app.route('/13')
def top_10_cheapest_kiwi():
    """In which period was 1 kg kiwi cheapest and what was the price? (Show top 10)"""
    return


@bv.app.route('/14')
def top_10_most_expensive_kiwi():
    """In which period was 1 kg kiwi most expensive and what was the price? (Show top 10)"""
    return


@bv.app.route('/18')
def line_chart_displayed():
    """Function which uses the LinePlot class in line_chart_plot.py """
    # Creates a new instance of the LinePlot(Self) and binds it to NewLCI
    newLCI = lcp.LinePlot()
    # linceCC uses the create_line_chart method to create a new chart
    lineCC = newLCI.create_line_chart(title='Pris historik', period=tomatoes['Period'].iloc[0:10])
    # renders the line chart
    return lineCC.render_response()


bv.run_program()


"""RUN THE METHODS IN COMMAND LINE
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

"""
#---------------------------TEST OTHER POSSIBILITIES NOT IN USE---------------------------------------------
period = df['Series_reference'][0:10].str.split(',')
print(period)


#Choose specific columns
#columns = df[df.columns[1:3]][0:10]
#print(pd.DataFrame(columns))
"""
