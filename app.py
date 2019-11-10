# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:15:45 2019

@author: ChAnDu_AB
"""

from flask import Flask,request, jsonify,render_template
import pickle
import numpy as np

"Defining the app and importing the model"
app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

"Applicaion"

@app.route('/')
def home():
    return render_template('index.html')

"It will hit the predict method "
@app.route('/predict',methods=['POST'])  
def predict():
    "Reading the inputs from html"
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html',prediction_text='Employee Salary Should be ${}'.format(output))
    
    
if __name__ == "__main__" :
    app.run(debug=True)
