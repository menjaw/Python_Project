import pandas as pd
import web_view as wv
import pygal

df = pd.read_csv('food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv', sep='\t')

# Initilize program from App
wv.initialize()


# Create dictionary with the wanted columns
data = {
    'ref': df['Series_reference'],
    'Period': df['Period'],
    'Price': df['Data_value'],
    'Product': df['Series_title_1'],
    'Amount': 0
}


@wv.app.route('/')
def show_data():
    return wv.render_template('index.html', data=df.to_html())


@wv.app.route('/1')
def total_products_investigated():
    """Question 1 - How many products have been tested?"""
    total_amount = len(df.drop_duplicates(['Series_title_1']))
    return wv.render_template('index.html', data=total_amount.to_html())


@wv.app.route('/2')
def single_product_investigated():
    """Question 2 - How many times have each product been tested?"""
    # Put columns together
    frame = pd.DataFrame(data, columns=['Product', 'Amount'])

    amount = frame.groupby(['Product']).count()
    return wv.render_template('index.html', data=amount.to_html())


@wv.app.route('/3')
def year_of_cheapest_tuna():
    """Question 3 - When was 'Tuna - canned' cheapest?"""
    frame = pd. DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    cheapest = tuna.sort_values(by="Price").head(1)
    return "The year of cheapest tuna is: " + wv.render_template('index.html', data=cheapest.to_html())


@wv.app.route('/4')
def year_of_most_expensive_tuna():
    """Question 4 - When was 'Tuna - canned' most expensive?"""
    frame = pd. DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    expensive = tuna.sort_values(by="Price", ascending=False).head(1)
    return wv.render_template('index.html', data=expensive.to_html())


@wv.app.route('/5')
def most_cheapest_product():
    """Question 5 - Show the most cheapest products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    cheapest = frame.sort_values(by='Price', ascending=True).head(1)
    return wv.render_template('index.html', data=cheapest.to_html())


@wv.app.route('/6')
def most_expensive_product():
    """Question 6 - Show the most expensive products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    expensive = frame.sort_values(by='Price', ascending=False).head(1)
    return wv.render_template('index.html', data=expensive.to_html())


@wv.app.route('/7')
def top_10_cheapest_products():
    """Question 7 - Show the top 10 cheapest food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(by='Price', ascending=True).drop_duplicates(subset='Product').head(10)
    return wv.render_template('index.html', data=filtered_frame.to_html())


@wv.app.route('/8')
def top_10_most_expensive_products():
    """Question 8 - Show the top 10 most expensive food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(by='Price', ascending=False).drop_duplicates('Product').head(10)
    return wv.render_template('index.html', data=filtered_frame.to_html())


@wv.app.route('/9')
def average_price_bananas_2012():
    """Question 9 - What was the average price for 1 kg bananas in 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (df.Period >= 2012.01) & (df.Period < 2013.01)]
    average = banana['Price'].mean()
    return wv.render_template('index.html', data=average.to_html())


@wv.app.route('/10')
def average_price_bananas_2013():
    """Question 10 - What was the average price for 1 kg bananas in 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)]
    average = banana['Price'].mean()
    return wv.render_template('index.html', data=average.to_html())


@wv.app.route('/11')
def price_for_carrots_march_2012():
    """Question 11 - What was the price for 1 kg carrots in marts 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(df.Series_title_1 == "Carrots, 1kg") & (df.Period == 2012.03)]
    return wv.render_template('index.html', data=carrot.to_html())


@wv.app.route('/12')
def price_for_carrots_march_2013():
    """Question 12 - What was the price for 1 kg carrots in marts 2013?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(df.Series_title_1 == "Carrots, 1kg") & (df.Period == 2013.03)]
    return wv.render_template('index.html', data=carrot.to_html())


@wv.app.route('/13')
def kiwi_prices_2013():
    """Show prices for kiwi in 2013"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    kiwi = frame[(df.Series_title_1 == "Kiwifruit, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)]\
        .sort_values(by='Price')
    return wv.render_template('index.html', data=kiwi.to_html())


@wv.app.route('/14')
def top_10_most_expensive_kiwi():
    """In which period was 1 kg kiwi most expensive and what was the price? (Show top 10)"""
    frame = pd.DataFrame(data, columns=['Price'])
    kiwi = frame[(df.Series_title_1 == "Kiwifruit, 1kg")].sort_values(by='Price', ascending=False)
    return wv.render_template('index.html', data=kiwi.to_html())


@wv.app.route('/15')
def apple_prices_2013():
    """Show prices for apples in 2013"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    apple = frame[(df.Series_title_1 == "Apples, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)].sort_values(
        by='Price')
    return wv.render_template('index.html', data=apple.to_html())


@wv.app.route('/16')
def banana_prices_2013():
    """Show prices for bananas in 2013"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)].sort_values(
        by='Price')
    return wv.render_template('index.html', data=banana.to_html())


@wv.app.route('/17')
def lettuce_prices_2013():
    """Show prices for lettuce in 2013"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    lettuce = frame[(df.Series_title_1 == "Lettuce, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)].sort_values(
        by='Price')
    return wv.render_template('index.html', data=lettuce.to_html())


@wv.app.route('/test')
def test():
    """Show prices for lettuce in 2013"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    lettuce = frame[(df.Series_title_1 == "Soup, canned, 500g")
                    & (df.Period >= 2017.01) & (df.Period < 2018.01)].sort_values(
        by='Period')
    return wv.render_template('index.html', data=lettuce.to_html())


@wv.app.route('/box-fruit-2013')
def box_fruit_2013():
    """Show the product prices in 2013"""
    box_plot = pygal.Box()
    box_plot.title = 'Fruit prices in 2013'
    box_plot.add('Kiwi, 1 kg', [1.90, 1.97, 2.00, 2.07, 2.32, 2.45, 3.16, 4.38, 4.73, 5.12, 5.96, 6.19])
    box_plot.add('Apple, 1 kg', [2.25, 2.33, 2.37, 2.41, 2.56, 2.58, 2.72, 2.96, 3.24, 3.60, 3.81, 4.12])
    box_plot.add('Banana, 1 kg', [2.53, 2.54, 2.55, 2.56, 2.64, 2.65, 2.67, 2.67, 2.67, 2.68, 2.78, 2.80])
    box_plot.add('Lettuce, 1 kg', [2.55, 2.61, 2.77, 2.85, 3.07, 3.56, 3.65, 3.74, 4.23, 6.56, 6.73, 9.18])
    box_plot.render()
    return box_plot.render_response()


@wv.app.route('/graph-canned-2017')
def graph_canned_2017():
    """Show prices at canned food in 2017"""
    graph = pygal.Line()
    graph.title = 'Prices on canned food in 2017'
    graph.x_label = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                     "Aug", "Sep", "Oct", "Nov", "Dec"]
    graph.add('Tuna, 185g', [2.52, 2.48, 2.50, 2.39, 2.60, 2.46, 2.53, 2.46, 2.39, 2.50, 2.58, 2.47])
    graph.add('Peaches, 410g', [1.65, 1.64, 1.62, 1.53, 1.66, 1.57, 1.56, 1.65, 1.59, 1.39, 1.58, 1.44])
    graph.add('Spaghetti, 420 g', [1.53, 1.56, 1.52, 1.40, 1.41, 1.45, 1.33, 1.47, 1.47, 1.42, 1.51, 1.50])
    graph.add('Tomato sauce, 560g', [3.15, 2.96, 2.90, 2.58, 2.99, 2.82, 2.64, 2.84, 2.92, 2.71, 2.78, 2.84])
    graph.add('Soup 500g', [3.46, 3.36, 3.18, 2.92, 2.91, 2.81, 2.79, 2.76, 2.72, 3.31, 3.42, 3.49])
    return graph.render_response()


@wv.app.route('/hist-product-count')
def hist_product_count():
    """Show how many times each product have been tested (ref question 2)"""
    hist = pygal.Histogram()
    hist.title = 'Count of how many time each product have been tested'
    hist.add('Apples, 1kg', [(142, 0, 1)])
    hist.add('Apricots, dried, 100g', [(81, 1, 2)])
    hist.add('Avocado, 1kg', [(134, 2, 3)])
    hist.add('Bacon - middle rashers, 700g', [(46, 3, 4)])
    hist.add('Beef steak - blade, 1kg', [(142, 4, 5)])
    hist.add('Berries, frozen, 500g', [(134, 5, 6)])
    hist.add('Breakfast drink, 250ml, 6 pack', [(45, 6, 7)])
    hist.add('Fresh herbs, packaged, chilled', [(6, 7, 8)])
    return hist.render_response()


@wv.app.route('/world-map')
def show_map():
    """Show the countries where the products have been tested"""
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Food prices in the world'
    worldmap_chart.add('New Zealand', ['nz'])
    return worldmap_chart.render()


wv.run_program()


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