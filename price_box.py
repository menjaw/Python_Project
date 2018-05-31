import run as r
from flask import Flask
import pygal


# initialize program
app = Flask(__name__)


@app.route('/box-fruit-2013')
def show_box_fruit_2013():
    box_plot = pygal.Box()
    box_plot.title = 'Fruit prices in 2013'
    box_plot.add('Kiwi, 1 kg', [1.90, 1.97, 2.00, 2.07, 2.32, 2.45, 3.16, 4.38, 4.73, 5.12, 5.96, 6.19])
    box_plot.add('Apple, 1 kg', [2.25, 2.33, 2.37, 2.41, 2.56, 2.58, 2.72, 2.96, 3.24, 3.60, 3.81, 4.12])
    box_plot.add('Banana, 1 kg', [2.53, 2.54, 2.55, 2.56, 2.64, 2.65, 2.67, 2.67, 2.67, 2.68, 2.78, 2.80])
    box_plot.add('Lettuce, 1 kg', [2.55, 2.61, 2.77, 2.85, 3.07, 3.56, 3.65, 3.74, 4.23, 6.56, 6.73, 9.18])
    box_plot.render()
    return box_plot.render_response()


@app.route('/graph-tuna')
def show_graph_tuna():
    graph = pygal.Line()
    graph.title('Price by year')
    graph.x_label = [2007.06, 2008.01, 2008.02, 2008.03, 2008.04]
    return graph.render_response()


# run program
#app.run(debug=True, port=3000)
