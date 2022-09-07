from flask import Flask, render_template, request, send_file
from result import Result, from_result_num
from flask.wrappers import Response
from leptoclassifier.lepto_classifier import LeptoClassifier
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Return the index.html file
    return render_template('index.html')

@app.route("/index.css")
def css():
     return send_file('css/index.css', mimetype='text/css')

@app.route("/lepto.css")
def style():
     return send_file('css/lepto.css', mimetype='text/css')

@app.route("/contact.css")
def style_c():
     return send_file('css/contact.css', mimetype='text/css')

@app.route("/help.css")
def style_h():
     return send_file('css/help.css', mimetype='text/css')

@app.route("/result.css")
def style_r():
     return send_file('css/result.css', mimetype='text/css')

#make router for the png/pictures, this uses send_file technique 
@app.route("/vet_pic.png")
def vet_pic():
     return send_file('templates/vet_pic.png', mimetype='image/png')

@app.route('/home')
def home():
    # Return the index.html file
    return render_template('index.html')

#make te router for the result, it will head to result.html
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

@app.route("/submit_data", methods=['POST'])
def submit_data():
    request_data = request.form
    print(request_data);
    df = pd.DataFrame(request_data.to_dict(flat=False), index=[0])
    df = df.apply(pd.to_numeric, errors='ignore')
    lepto_classifier = LeptoClassifier()
    try:
        prediction = lepto_classifier.predict_raw(df, use_mat=True);
        print("Prediction = " + str(prediction[0]));
    except (ValueError, KeyError) as err:
        return Response('{"status": "error", "message": "'+ str(err) + '"}', status=400)
    result = from_result_num(prediction[0])
    return Response('{"status": "ok", "result": "' + str(prediction[0]) + '"}', status=200)
