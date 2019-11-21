# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:59:06 2019

@author: AdilDSW
"""

import io
import os
import json

from flask import Flask, render_template, request, send_file

from generator import Generator
from predictor import Predictor

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/airpressure')
def airpressure():

    return render_template('airpressure.html')

@app.route('/pump')
def pump():

    return render_template('pump.html')
	
@app.route('/generate', methods=['GET'])
def generatorAPI():
    model = request.args.get('model')
    class_type = request.args.get('class_type')
    
    genObj = Generator()
    generated_data = genObj.generate(model, class_type)
    
    output = io.BytesIO()
    output.write(generated_data.encode('utf-8'))
    output.seek(0)
    
    return send_file(output, as_attachment=True, 
                     attachment_filename="{}_generated.txt".format(model))

@app.route('/predict', methods=['GET'])
def predictorAPI():
    model = request.args.get('model')
    data = request.args.get('data')
    
    preObj = Predictor()
    prediction = preObj.predict(model, data)
    
    return str(prediction)
    

if __name__ == "__main__":
    config = {'ip': '127.0.0.1', 'port': '8888'}
    
    if os.path.exists('config.json'):
        with open('config.json') as config_file:
            config = json.load(config_file)
    
    app.debug = True
    app.run(host=config['ip'], port=config['port'], use_reloader=False)