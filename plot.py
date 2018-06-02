import pygal
import pandas as pd

def exec_plot1(df):    
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
    # return the pie chart to the page
    return pie_chart

# filter the food price
def filter_price(cat, period,df):
    foods_mask = (df['Series_title_1'] == cat) & (df['Period'] == period)
    foods_df = df[foods_mask]  
    foods_price = float(foods_df['Data_value'].values)
    return foods_price

def exec_plot2():
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
    return hist