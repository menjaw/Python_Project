import pygal
import pandas as pd


df = pd.read_csv('food-price-index-mar18-weighted-average-prices-csv-tables.csv.tsv', sep='\t')

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



class LinePlot(object):
    """A line plot that shows a diagram of a desired dataset.

    Methods:
    create
    """

    def __init__(self):
        """Prints 'We'r Rolling to check if the class is instaciatet'"""
        print("We'r rolling")

    def create_line_chart(self, title, period):
        """A method which creates a new line chart

        PARAMETERS:
        Self

        TO DO:
        Make dynamic, meaning it should take the data provided by the dataset
        """
        line_chart = pygal.Line()
        line_chart.title = '{}'.format(title)
        line_chart.x_labels = map(str, period)
        line_chart.add('Tomatoes', tomatoes['Price'].iloc[0:10])
        line_chart.add('Cabbage', cabbage['Price'].iloc[0:10])
        line_chart.add('Lettuce', lettuce['Price'].iloc[0:10])
        line_chart.add('Orange',  oranges['Price'].iloc[0:10])
        return line_chart
