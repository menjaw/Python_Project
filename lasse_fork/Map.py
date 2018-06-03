import pandas as pan
import Pygal_generator as pg
import pycountry

daFrame = pan.read_csv("./data/mapData.csv")

def execMap():
    countryList = daFrame[daFrame.columns[0]].tolist()
    valueList = daFrame[daFrame.columns[1]].tolist()

    mapDict = dict(zip(countryList, valueList))

    converted = convertCountry(mapDict)

    map = pg.createMap(title="Interactive Banana World Map", data=converted)
    return map


'''Convert country names to country ISO 3166-1 alpha-2 or country abbreviations '''
def convertCountry(input):
    alpha2 = {}

    for key, value in input.items():
        try:
            temp = pycountry.countries.get(name=key).alpha_2
            alpha2[temp.lower()] = value
        except:
            pass
        else:
            pass
    return alpha2
