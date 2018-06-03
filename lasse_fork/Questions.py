import pandas as pan
import Pygal_generator as pg

dFrame = pan.read_csv("./data/NZ_DataSet.csv.tsv", sep='\t')

'''til menjas besvarelser, original hed dataframet df ikke dFrame'''
data = {
    'ref': dFrame['Series_reference'],
    'Period': dFrame['Period'],
    'Price': dFrame['Data_value'],
    'Product': dFrame['Series_title_1'],
    'Amount': 0
}


'''Skal der tilfoejes et question, tilfoejes det her, formattet er: {webpage:[question, thumb-URL]}'''
def getQuestions():
    questions = {1:["How many products have been tested?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                2:["How many times have each product been tested?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                3:["When was 'Tuna - canned' cheapest?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                4:["When was 'Tuna - canned' most expensive?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                5:["Show the most cheapest product.", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                6:["Show the most expensive product.", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                7:["Show the top 10 cheapest food products", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                8:["Show the top 10 most expensive food products.", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                9:["What was the average price for 1 kg bananas in 2012?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                10:["What was the average price for 1 kg bananas in 2013?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                11:["What was the price for 1 kg carrots in marts 2012?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                12:["What was the price for 1 kg carrots in marts 2013?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                13:["In which period was 1 kg kiwi cheapestand what was the price (Show top 10)?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                14:["In which period was 1 kg kiwi most expensive and what was the price (Show top 10)?", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                15:["Show prices for apples in 2013", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                15:["Show prices for bananas in 2013", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                15:["Show prices for lettuce in 2013", "https://cdn0.iconfinder.com/data/icons/file-types-22/64/file_txt-128.png"],
                18:["Show a comparison of Banana, Apple and Orange prices through the years", "http://www.iconarchive.com/download/i87059/graphicloads/colorful-long-shadow/Chart-pie.ico"],
                19:["Show a comparison of food prices in 2017 in %", "http://www.iconarchive.com/download/i87059/graphicloads/colorful-long-shadow/Chart-pie.ico"]
                }
    return questions

'''Her kan der skrives custom logic til forskellige questions'''


def execQ1():
    '''Question 1 - How many products have been tested?'''
    total_amount = len(dFrame.drop_duplicates(['Series_title_1']))
    return total_amount

def execQ2():
    """Question 2 - How many times have each product been tested?"""
    # Put columns together
    frame = pan.DataFrame(data, columns=['Product', 'Amount'] )
    amount = frame.groupby(['Product']).count()
    return amount

def execQ3():
    """Question 3 - When was 'Tuna - canned' cheapest?"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[dFrame.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    cheapest = tuna.sort_values(by="Price").head(1)
    return cheapest

def execQ4():
    """Question 4 - When was 'Tuna - canned' most expensive?"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[dFrame.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    expensive = tuna.sort_values(by="Price", ascending=False).head(1)
    return expensive

def execQ5():
    """Question 5 - Show the most cheapest products"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    cheapest = frame.sort_values(by='Price', ascending=True).head(1)
    return cheapest

def execQ6():
    """Question 6 - Show the most expensive products"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    expensive = frame.sort_values(by='Price', ascending=False).head(1)
    return expensive

def execQ7():
    """Question 7 - Show the top 10 cheapest food products"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(by='Price', ascending=True).drop_duplicates(subset='Product').head(10)
    return filtered_frame

def execQ8():
    """Question 8 - Show the top 10 most expensive food products"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(by='Price', ascending=False).drop_duplicates('Product').head(10)
    return filtered_frame

def execQ9():
    """Question 9 - What was the average price for 1 kg bananas in 2012?"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(dFrame.Series_title_1 == "Bananas, 1kg") & (dFrame.Period >= 2012.01) & (dFrame.Period < 2013.01)]
    average = banana['Price'].mean()
    return average

def execQ10():
    """Question 10 - What was the average price for 1 kg bananas in 2013?"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(dFrame.Series_title_1 == "Bananas, 1kg") & (dFrame.Period >= 2013.01) & (dFrame.Period < 2014.01)]
    average = banana['Price'].mean()
    return average

def execQ11():
    """Question 11 - What was the price for 1 kg carrots in marts 2012?"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(dFrame.Series_title_1 == "Carrots, 1kg") & (dFrame.Period == 2012.03)]
    return carrot

def execQ12():
    """Question 12 - What was the price for 1 kg carrots in marts 2013?"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(dFrame.Series_title_1 == "Carrots, 1kg") & (dFrame.Period == 2013.03)]
    return carrot

def execQ13():
    """Show prices for kiwi in 2013"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    kiwi = frame[(dFrame.Series_title_1 == "Kiwifruit, 1kg") & (dFrame.Period >= 2013.01) & (dFrame.Period < 2014.01)]\
        .sort_values(by='Price')
    return kiwi

def execQ14():
    """In which period was 1 kg kiwi most expensive and what was the price? (Show top 10)"""
    frame = pan.DataFrame(data, columns=['Price'])
    kiwi = frame[(dFrame.Series_title_1 == "Kiwifruit, 1kg")].sort_values(by='Price', ascending=False)
    return kiwi

def execQ15():
    """Show prices for apples in 2013"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    apple = frame[(dFrame.Series_title_1 == "Apples, 1kg") & (dFrame.Period >= 2013.01) & (dFrame.Period < 2014.01)].sort_values(
        by='Price')
    return apple

def execQ16():
    """Show prices for bananas in 2013"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(dFrame.Series_title_1 == "Bananas, 1kg") & (dFrame.Period >= 2013.01) & (dFrame.Period < 2014.01)].sort_values(
        by='Price')
    return banana

def execQ17():
    """Show prices for lettuce in 2013"""
    frame = pan.DataFrame(data, columns=['Product', 'Price', 'Period'])
    lettuce = frame[(dFrame.Series_title_1 == "Lettuce, 1kg") & (dFrame.Period >= 2013.01) & (dFrame.Period < 2014.01)].sort_values(
        by='Price')
    return lettuce





def execQ18():

    oranges_mask = (dFrame['Series_title_1'] == 'Oranges, 1kg') & (dFrame['Period'] >= 2003)& (dFrame['Period'] <= 2013)
    bananas_mask = (dFrame['Series_title_1'] == 'Bananas, 1kg') & (dFrame['Period'] >= 2003)& (dFrame['Period'] <= 2013)
    apples_mask = (dFrame['Series_title_1'] == 'Apples, 1kg') & (dFrame['Period'] >= 2003)& (dFrame['Period'] <= 2013)
    oranges_data = dFrame[oranges_mask]
    bananas_data = dFrame[bananas_mask]
    apples_data = dFrame[apples_mask]
    oranges_res = oranges_data['Data_value'][:11].values
    bananas_res = bananas_data['Data_value'][:11].values
    apples_res = apples_data['Data_value'][:11].values

    data = {"Oranges":oranges_res,
                "Bananas":bananas_res,
                "Apples":apples_res}

    chart = pg.createBar(data, "Frugt prices per kg between 2003 - 2013")

    return chart

def execQ19():
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
    a_price = filter_price(a_cat,period,dFrame)
    b_price = filter_price(b_cat,period,dFrame)
    c_price = filter_price(c_cat,period,dFrame)
    d_price = filter_price(d_cat,period,dFrame)
    e_price = filter_price(e_cat,period,dFrame)
    f_price = filter_price(f_cat,period,dFrame)
    g_price = filter_price(g_cat,period,dFrame)
    h_price = filter_price(h_cat,period,dFrame)
    i_price = filter_price(i_cat,period,dFrame)
    j_price = filter_price(j_cat,period,dFrame)

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

    data = {a_title:a_pct,
    b_title:b_pct,
    c_title:c_pct,
    d_title:d_pct,
    e_title:e_pct,
    f_title:f_pct,
    g_title:g_pct,
    h_title:h_pct,
    i_title:i_pct,
    j_title:j_pct
    }

    chart = pg.createPie(data, "Comparison food price in 2017 in %")

    return chart


# filter the food price
def filter_price(cat, period,dFrame):
    foods_mask = (dFrame['Series_title_1'] == cat) & (dFrame['Period'] == period)
    foods_df = dFrame[foods_mask]
    foods_price = float(foods_df['Data_value'].values)
    return foods_price
