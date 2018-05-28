import pandas as pd
from flask import Flask, render_template
import pygal
#import piePlot

"""Series_reference	Period	Data_value	STATUS	UNITS	Subject	Group	Series_title_1"""
# sep ='/t' is a variable which tell pandas is tabs not commans
df = pd.read_csv('food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv', sep='\t')

#Initilize program from App
app = Flask(__name__)


@app.route('/plot')
def show_data():
    period = 2018.03

    # Possible to change other catgory
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

    a_res = calculator(a_cat,period)
    b_res = calculator(b_cat,period)
    c_res = calculator(c_cat,period)
    d_res = calculator(d_cat,period)
    e_res = calculator(e_cat,period)
    f_res = calculator(f_cat,period)
    g_res = calculator(g_cat,period)
    h_res = calculator(h_cat,period)
    i_res = calculator(i_cat,period)
    j_res = calculator(j_cat,period)

    total = a_res+b_res+c_res+d_res+e_res+f_res+g_res+h_res+i_res+j_res 
    a_pct = round((a_res / total)*100,2)
    b_pct = round((b_res / total)*100,2)
    c_pct = round((c_res / total)*100,2)
    d_pct = round((d_res / total)*100,2)
    e_pct = round((e_res / total)*100,2)
    f_pct = round((f_res / total)*100,2)
    g_pct = round((g_res / total)*100,2)
    h_pct = round((h_res / total)*100,2)
    i_pct = round((i_res / total)*100,2)
    j_pct = round((j_res / total)*100,2)

    a_title = '1 kg oranges - Price: {}$'.format(a_res)
    b_title = '1 kg bananas - Price: {}$'.format(b_res)
    c_title = '1 kg apples - Price: {}$'.format(c_res)
    d_title = '1 kg kiwifruit - Price: {}$'.format(d_res)
    e_title = '1 kg carrots - Price: {}$'.format(e_res)
    f_title = '1 kg potatoes - Price: {}$'.format(f_res)
    g_title = '1 kg celery - Price: {}$'.format(g_res)
    h_title = '1 kg cauliflower - Price: {}$'.format(h_res)
    i_title = '1 kg beans - Price: {}$'.format(i_res)
    j_title = '1 kg avocado - Price: {}$'.format(j_res)

    ## pygal
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

    #return render_template('pie.html', data = lst_pct, name = title)
    return pie_chart.render_response()


def calculator(cat, period):
    organges_mask = (df['Series_title_1'] == cat) & (df['Period'] == period)
    organges_df = df[organges_mask]  
    organges_price = float(organges_df['Data_value'].values)
    return organges_price

app.run(debug=True, port=3000)

