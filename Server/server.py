from flask import Flask
from flask import request
from flask import jsonify
import utils

app = Flask(__name__)

@app.route('/hello')
def hello():
    return("Flask server")

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : utils.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_area_names')
def get_area_names():
    response = jsonify({
        'areas' : utils.get_areas_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price' , methods = ['GET' , 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath']) 
    area = request.form['area']

    # total_sqft = 1000
    # location = 'Indira Nagar'
    # bhk = 4
    # bath = 3 
    # area = 'Plot Area' 

    response = jsonify({
        'estimated_price' : utils.get_estimated_price(bath , bhk , total_sqft , area , location)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    # print(response)
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction.....")
    utils.load_saved_artifacts()
    app.run()