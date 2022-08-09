from flask import Flask, render_template, request, Response, send_file
from leptoclassifier.lepto_classifier import LeptoClassifier
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Return the index.html file
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/lepto')
def lepto():
    return render_template('lepto.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/index.css")
def css():
    return send_file('templates/index.css', mimetype='text/css')

@app.route("/vet_pic.png")
def vet_pic():
    return send_file('templates/vet_pic.png', mimetype='image/png')

@app.route("/submit_data", methods=['POST'])
def submit_data():
    request_data = request.form
    df = pd.DataFrame(request_data.to_dict(flat=False), index=[0])
    df = df.apply(pd.to_numeric, errors='ignore')
    lepto_classifier = LeptoClassifier()
    try:
        prediction = lepto_classifier.predict_raw(df, use_mat=True);
        print("Prediction = " + str(prediction[0]));
    except (ValueError, KeyError) as err:
        return Response('{"status": "error", "message": "'+ str(err) + '"}', status=400)
    return Response('{"status": "ok", "result": "' + str(prediction[0]) + '"}', status=200)
