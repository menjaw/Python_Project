import pandas as pd

def exec_qst1(df):
    """Question 1 - How many products have been tested?"""
    total_amount = len(df.drop_duplicates(['Series_title_1']))
    return total_amount

def exec_qst2(data):
    """Question 2 - How many times have each product been tested?"""
    # Put columns together
    frame = pd.DataFrame(data, columns=['Product', 'Amount'] )
    amount = frame.groupby(['Product']).count()
    return amount

def exec_qst3(data,df):
    """Question 3 - When was 'Tuna - canned' cheapest?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    cheapest = tuna.sort_values(by="Price").head(1)
    return cheapest

def exec_qst4(data,df):
    """Question 4 - When was 'Tuna - canned' most expensive?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    tuna = frame[df.Series_title_1 == "Tuna - canned (supermarket only), 185g"]
    expensive = tuna.sort_values(by="Price", ascending=False).head(1)
    return expensive

def exec_qst5(data):
    """Question 5 - Show the most cheapest products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    cheapest = frame.sort_values(by='Price', ascending=True).head(1)
    return cheapest

def exec_qst6(data):
    """Question 6 - Show the most expensive products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    expensive = frame.sort_values(by='Price', ascending=False).head(1)
    return expensive

def excec_qst7(data):
    """Question 7 - Show the top 10 cheapest food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(by='Price', ascending=True).drop_duplicates(subset='Product').head(10)
    return filtered_frame

def excec_qst8(data):
    """Question 8 - Show the top 10 most expensive food products"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    filtered_frame = frame.sort_values(by='Price', ascending=False).drop_duplicates('Product').head(10)
    return filtered_frame

def excec_qst9(data,df):
    """Question 9 - What was the average price for 1 kg bananas in 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (df.Period >= 2012.01) & (df.Period < 2013.01)]
    average = banana['Price'].mean()
    return average

def excec_qst10(data,df):
    """Question 10 - What was the average price for 1 kg bananas in 2013?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)]
    average = banana['Price'].mean()
    return average

def excec_qst11(data,df):
    """Question 11 - What was the price for 1 kg carrots in marts 2012?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(df.Series_title_1 == "Carrots, 1kg") & (df.Period == 2012.03)]
    return carrot

def excec_qst12(data,df):
    """Question 12 - What was the price for 1 kg carrots in marts 2013?"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    carrot = frame[(df.Series_title_1 == "Carrots, 1kg") & (df.Period == 2013.03)]
    return carrot

def excec_qst13(data,df):
    """Show prices for kiwi in 2013"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    kiwi = frame[(df.Series_title_1 == "Kiwifruit, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)]\
        .sort_values(by='Price')
    return kiwi

def excec_qst14(data,df):
    """In which period was 1 kg kiwi most expensive and what was the price? (Show top 10)"""
    frame = pd.DataFrame(data, columns=['Price'])
    kiwi = frame[(df.Series_title_1 == "Kiwifruit, 1kg")].sort_values(by='Price', ascending=False)
    return kiwi

def excec_qst15(data,df):
    """Show prices for apples in 2013"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    apple = frame[(df.Series_title_1 == "Apples, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)].sort_values(
        by='Price')
    return apple

def excec_qst16(data,df):
    """Show prices for bananas in 2013"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    banana = frame[(df.Series_title_1 == "Bananas, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)].sort_values(
        by='Price')
    return banana

def excec_qst17(data,df):
    """Show prices for lettuce in 2013"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    lettuce = frame[(df.Series_title_1 == "Lettuce, 1kg") & (df.Period >= 2013.01) & (df.Period < 2014.01)].sort_values(
        by='Price')
    return lettuce 

def excec_test(data,df):
    """Show prices for 500g canned Soup in 2017"""
    frame = pd.DataFrame(data, columns=['Product', 'Price', 'Period'])
    lettuce = frame[(df.Series_title_1 == "Soup, canned, 500g")
                    & (df.Period >= 2017.01) & (df.Period < 2018.01)].sort_values(
        by='Period')
    return lettuce