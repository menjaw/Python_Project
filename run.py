import pandas as pd
import web_view as wv
import pygal
import plot as pt
import questions as qst

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
def home_page():
    return wv.render_template('index.html')

@wv.app.route('/answers')
def show_answers():
    return wv.render_template('answers.html')

@wv.app.route('/plot')
def plot_page():
    return wv.render_template('plot.html')

@wv.app.route('/info')
def info_page():
    return wv.render_template('info.html')

@wv.app.route('/data')
def show_data():
    return wv.render_template('answers.html', data=df.to_html())

@wv.app.route('/1')
def total_products_investigated():
    title= 'The number of products have been tested'
    result = qst.exec_qst1(df)
    return wv.render_template('answers.html', data=result, title = title )

@wv.app.route('/2')
def single_product_investigated():
    title= 'The number of each product have been tested'
    amount = qst.exec_qst2(data)
    return wv.render_template('answers.html', data=amount.to_html(), title = title )

@wv.app.route('/3')
def year_of_cheapest_tuna():
    title= 'The year of cheapest tuna was'
    cheapest = qst.exec_qst3(data,df)
    return  wv.render_template('answers.html', data=cheapest.to_html(), title = title)

@wv.app.route('/4')
def year_of_most_expensive_tuna():
    title= 'The year of most expensive tuna was:'
    expensive = qst.exec_qst4(data,df)
    return wv.render_template('answers.html', data=expensive.to_html(), title = title)

@wv.app.route('/5')
def most_cheapest_product():
    title= 'The most cheapest product is'
    cheapest = qst.exec_qst5(data)
    return wv.render_template('answers.html', data=cheapest.to_html(), title = title )

@wv.app.route('/6')
def most_expensive_product():
    title = 'The most expensive product is'
    expensive = qst.exec_qst6(data)
    return wv.render_template('answers.html', data=expensive.to_html(), title = title)

@wv.app.route('/7')
def top_10_cheapest_products():
    title = 'The list of top 10 cheapest food products'
    filtered_frame = qst.excec_qst7(data)
    return wv.render_template('answers.html', data=filtered_frame.to_html(), title = title)

@wv.app.route('/8')
def top_10_most_expensive_products():
    title = 'The list of top 10 most expensive food products'
    filtered_frame = qst.excec_qst8(data)
    return wv.render_template('answers.html', data=filtered_frame.to_html(), title = title)

@wv.app.route('/9')
def average_price_bananas_2012():
    title = 'The average price for 1 kg bananas in 2012 is ($)'
    average = qst.excec_qst9(data,df)
    return wv.render_template('answers.html', data=round(average,3), title = title)

@wv.app.route('/10')
def average_price_bananas_2013():
    title = 'The average price for 1 kg bananas in 2013 is ($)'
    average = qst.excec_qst10(data,df)
    return wv.render_template('answers.html', data=round(average,3), title = title)

@wv.app.route('/11')
def price_for_carrots_march_2012():
    title = 'The price for 1 kg carrots in marts 2012 is ($)'
    carrot = qst.excec_qst11(data,df)
    return wv.render_template('answers.html', data=carrot.to_html(), title = title)

@wv.app.route('/12')
def price_for_carrots_march_2013():
    title = 'The price for 1 kg carrots in marts 2013 is ($)'
    carrot = qst.excec_qst12(data,df)
    return wv.render_template('answers.html', data=carrot.to_html(), title = title)

@wv.app.route('/13')
def kiwi_prices_2013():
    title = 'The list of prices for kiwi in 2013 ($)'
    kiwi = qst.excec_qst13(data,df)
    return wv.render_template('answers.html', data=kiwi.to_html(), title = title)

@wv.app.route('/14')
def top_10_most_expensive_kiwi():
    title = 'The top 10 most expensive list of kiwi (1 kg)'
    kiwi = qst.excec_qst14(data,df)
    return wv.render_template('answers.html', data=kiwi[:10].to_html(), title= title)

@wv.app.route('/15')
def apple_prices_2013():
    title = 'The prices for apples in 2013'
    apple = qst.excec_qst15(data,df)
    return wv.render_template('answers.html', data=apple.to_html(), title = title)

@wv.app.route('/16')
def banana_prices_2013():
    title = 'The prices for bananas in 2013'
    banana = qst.excec_qst16(data,df)
    return wv.render_template('answers.html', data=banana.to_html(), title = title )

@wv.app.route('/17')
def lettuce_prices_2013():
    title = 'The prices for lettuce in 2013'
    lettuce = qst.excec_qst17(data,df)
    return wv.render_template('answers.html', data=lettuce.to_html(), title = title)

@wv.app.route('/test')
def test():
    title = 'The prices for 500g canned Soup in 2017'
    lettuce = qst.excec_test(data,df)
    return wv.render_template('answers.html', data=lettuce.to_html(), title = title)

@wv.app.route('/food_price_2017')
def food_price_2017():
    result = pt.exec_plot1(df)
    return wv.Response(response=result.render(),content_type='image/svg+xml')

@wv.app.route('/hist-product-count')
def hist_product_count():
    restult = pt.exec_plot2()
    return restult.render_response()

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