import pygal
import pandas as pd

def frugt_prices_2003_2013(df):
    line_chart = pygal.Bar()
    line_chart.title = 'Frugt prices per kg between 2003 - 2013 $'
    line_chart.x_labels = map(str, range(2003,2014))
    oranges_mask = (df['Series_title_1'] == 'Oranges, 1kg') & (df['Period'] >= 2003)& (df['Period'] <= 2013)
    bananas_mask = (df['Series_title_1'] == 'Bananas, 1kg') & (df['Period'] >= 2003)& (df['Period'] <= 2013)
    apples_mask = (df['Series_title_1'] == 'Apples, 1kg') & (df['Period'] >= 2003)& (df['Period'] <= 2013)
    oranges_data = df[oranges_mask]
    bananas_data = df[bananas_mask]
    apples_data = df[apples_mask]
    oranges_res = oranges_data['Data_value'][:11].values
    bananas_res = bananas_data['Data_value'][:11].values
    apples_res = apples_data['Data_value'][:11].values
    line_chart.add('Oranges',oranges_res)
    line_chart.add('Bananas',bananas_res)
    line_chart.add('Apples',apples_res)
    line_chart.render_to_file('./Plotting/frugt_prices_2003_2013.svg')   
    return line_chart

def food_prices_2017(df):    
    # choice a datetime
    period = 2018.03

    # possible to change other catgories
    a_cat = 'Oranges, 1kg'
    b_cat = 'Bananas, 1kg'
    c_cat = 'Apples, 1kg'
    d_cat = 'Kiwifruit, 1kg'
    e_cat = 'Carrots, 1kg'
    f_cat = 'Potatoes, 1kg'
    g_cat = 'Celery, 1kg'
    h_cat = 'Cauliflower, 1kg'
    i_cat = 'Beans, 1kg'
    j_cat = 'Avocado, 1kg'

    # return the price of food
    a_price = filter_price(a_cat,period,df)
    b_price = filter_price(b_cat,period,df)
    c_price = filter_price(c_cat,period,df)
    d_price = filter_price(d_cat,period,df)
    e_price = filter_price(e_cat,period,df)
    f_price = filter_price(f_cat,period,df)
    g_price = filter_price(g_cat,period,df)
    h_price = filter_price(h_cat,period,df)
    i_price = filter_price(i_cat,period,df)
    j_price = filter_price(j_cat,period,df)

    # total price
    total = a_price+b_price+c_price+d_price+e_price+f_price+g_price+f_price+i_price+j_price 
    
    # find % of those prices
    a_pct = round((a_price / total)*100,2)
    b_pct = round((b_price / total)*100,2)
    c_pct = round((c_price / total)*100,2)
    d_pct = round((d_price / total)*100,2)
    e_pct = round((e_price / total)*100,2)
    f_pct = round((f_price / total)*100,2)
    g_pct = round((g_price / total)*100,2)
    h_pct = round((h_price / total)*100,2)
    i_pct = round((i_price / total)*100,2)
    j_pct = round((j_price / total)*100,2)

    # titles
    a_title = '1 kg oranges - Price: {}$'.format(a_price)
    b_title = '1 kg bananas - Price: {}$'.format(b_price)
    c_title = '1 kg apples - Price: {}$'.format(c_price)
    d_title = '1 kg kiwifruit - Price: {}$'.format(d_price)
    e_title = '1 kg carrots - Price: {}$'.format(e_price)
    f_title = '1 kg potatoes - Price: {}$'.format(f_price)
    g_title = '1 kg celery - Price: {}$'.format(g_price)
    h_title = '1 kg cauliflower - Price: {}$'.format(h_price)
    i_title = '1 kg beans - Price: {}$'.format(i_price)
    j_title = '1 kg avocado - Price: {}$'.format(j_price)

    ## get pie from pygal
    pie_chart = pygal.Pie()
    pie_chart.title = 'Comparison food price in 2017 in %'
    pie_chart.add(a_title, a_pct)
    pie_chart.add(b_title, b_pct)
    pie_chart.add(c_title, c_pct)
    pie_chart.add(d_title, d_pct)
    pie_chart.add(e_title, e_pct)
    pie_chart.add(f_title, f_pct)
    pie_chart.add(g_title, g_pct)
    pie_chart.add(h_title, h_pct)
    pie_chart.add(i_title, i_pct)
    pie_chart.add(j_title, j_pct)
    pie_chart.render_to_file('./Plotting/foods_prices_2017.svg')  
    # return the pie chart to the page
    return pie_chart

# filter the food price
def filter_price(cat, period,df):
    foods_mask = (df['Series_title_1'] == cat) & (df['Period'] == period)
    foods_df = df[foods_mask]  
    foods_price = float(foods_df['Data_value'].values)
    return foods_price

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
    hist.render_to_file('./Plotting/hist_product_count.svg')   
    return hist

def box_fruit_2013():
    """Show the product prices in 2013"""
    box_plot = pygal.Box()
    box_plot.title = 'Fruit prices in 2013'
    box_plot.add('Kiwi, 1 kg', [1.90, 1.97, 2.00, 2.07, 2.32, 2.45, 3.16, 4.38, 4.73, 5.12, 5.96, 6.19])
    box_plot.add('Apple, 1 kg', [2.25, 2.33, 2.37, 2.41, 2.56, 2.58, 2.72, 2.96, 3.24, 3.60, 3.81, 4.12])
    box_plot.add('Banana, 1 kg', [2.53, 2.54, 2.55, 2.56, 2.64, 2.65, 2.67, 2.67, 2.67, 2.68, 2.78, 2.80])
    box_plot.add('Lettuce, 1 kg', [2.55, 2.61, 2.77, 2.85, 3.07, 3.56, 3.65, 3.74, 4.23, 6.56, 6.73, 9.18])
    box_plot.render_to_file('./Plotting/box_fruit_2013.svg')
    return box_plot

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
    graph.render_to_file('./Plotting/graph_canned_2017.svg')
    return graph

