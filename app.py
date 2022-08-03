from flask import Flask, render_template, request, Response
from leptoclassifier.lepto_classifier import LeptoClassifier
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Return the index.html file
    return render_template('index.html')

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
