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
    print(request_data);
    df = pd.DataFrame(request_data.to_dict(flat=False), index=[0])
    print(df);
    return Response("Ok!", status=200)
