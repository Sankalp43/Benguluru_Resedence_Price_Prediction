import json
import pickle
import numpy as np

__areas = None
__locations = None
__data_columns = None
__model = None


def get_estimated_price(bath , bhk , sqft , area , location):
    try:
        area_index = __data_columns.index(area.lower())
        loc_index = __data_columns.index(location.lower())
    except:
        area_index = -1
        loc_index = -1


    x = np.zeros(len(__data_columns))
    x[0] = bath
    x[1] = bhk
    x[2] = sqft
    if area_index>=0:
        x[area_index] = 1
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0] , 2)
    

def get_areas_names():
    # load_saved_artifacts()
    return __areas

def get_location_names():
    # load_saved_artifacts()
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts....start')
    global __data_columns
    global __locations
    global __areas
    global __model

    with open('./model accessory/columns.json' , 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[7:]
        __areas = __data_columns[3:7]

    with open('./model accessory/bangalore_residence_price_model.pickle' , 'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts.....done!")

if __name__ == '__main__':
    # get_location_names()
    load_saved_artifacts()
    # print(get_areas_names())
    # print(get_location_names())
    # print(get_estimated_price(3 , 4 , 1000 , 'Plot Area' , 'Indira Nagar'))
    # print(get_estimated_price(6 , 6 , 2000 , 'Plot Area' , 'Indira Nagar'))



