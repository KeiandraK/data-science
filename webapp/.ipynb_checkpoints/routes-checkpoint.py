from webapp import app
from flask import render_template
import pandas as pd
from flask import Flask, jsonify, request
import pickle
import json




@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/addthis', methods=['GET', 'POST'])
def addthis():
	return f"{10 + 5}"

def create_app():

    #load model
    model = pickle.load(open('model.pkl','rb'))

    # app
    app = Flask(__name__)
    app.config.webapp('iirs')


    # routes
    @app.route('/predict', methods=['POST'])

    def predict():
        # get data
        data = request.get_json(force=True)

        # convert data into dataframe
        data.update((x, [y]) for x, y in data.items())
        data_df = pd.DataFrame.from_dict(data)

        # predictions
        result = model.predict(data_df)

        # send back to browser
        output = {'results': int(result[0])}

        # return data
        return jsonify(results=output)

    @app.route('\test1', methods=['GET'])
    
    def give_data():
        
        return true
        