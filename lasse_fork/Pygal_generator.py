import pygal

def createPie(data, title):

    pie_chart = pygal.Pie()
    pie_chart.title = title
    for key, value in data.items():
        pie_chart.add(key,value)
    return pie_chart.render_data_uri()


'''Skulle vaere dynamisk med havde ikke mere tid'''
def createBar(data, title):
    line_chart = pygal.Bar()
    line_chart.title = title
    line_chart.x_labels = map(str, range(2003,2014))

    for key, value in data.items():
        line_chart.add(key,value)

    return line_chart.render_data_uri()






'''Takes a dictionary of countries and values'''
def createMap(title, data):

    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = title
    worldmap_chart.add('1kg Bananas in DKK', data)

    return worldmap_chart.render_data_uri()

    '''.render_to_file('./data/map.svg')'''
