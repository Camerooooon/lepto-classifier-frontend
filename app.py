from flask import Flask, render_template, request, send_file, redirect, url_for
from result import Result
from result_into_pdf import gen_pdf
from flask.wrappers import Response
import database as db
from leptoclassifier.lepto_classifier import LeptoClassifier
import pandas as pd
import random
import string

con = db.con_database();
cur = con.cursor();

db.init_database(cur);

app = Flask(__name__)

@app.route("/")
def main():
    # Return the intro.html file
    return render_template('main.html')

@app.route("/main.css")
def style_i():
     return send_file('css/main.css', mimetype='text/css')

@app.route("/index.css")
def css():
     return send_file('css/index.css', mimetype='text/css')

@app.route("/index.js")
def js():
     return send_file('js/index.js', mimetype='text/javascript')

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

@app.route("/doggo.mp4")
def dog_vid():
     return send_file('templates/doggo.mp4', mimetype='video/mp4')

@app.route("/dog.png")
def dog_pic():
     return send_file('templates/dog.png', mimetype='image/png')

#intro is the home page 
@app.route('/home')
def home():
    # Return the index.html file
    return render_template('main.html')

@app.route('/index')
def index():
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
     print("it is under construction")
     return render_template('index.html')

@app.route('/contact')
def contact():
     return render_template('contact.html')

@app.route("/submit_data", methods=['POST'])
def submit_data():
    request_data = request.form
    df = pd.DataFrame(request_data.to_dict(flat=False), index=[0])
    df = df.apply(pd.to_numeric, errors='ignore')
    lepto_classifier = LeptoClassifier()

    try:
        if request_data["MAT"] == "-1":
            df["MAT"] = 0;
            prediction = lepto_classifier.predict_raw(df, use_mat=False);
            print("Using no MAT prediction");
        else:
            prediction = lepto_classifier.predict_raw(df, use_mat=True);
            print("Using MAT prediction");
        print("Prediction = " + str(prediction[0]));
    except (ValueError, KeyError) as err:
        return Response('Internal Error (This is probably our fault, please contact us!): '+ str(err), status=400)
    except (IndexError):
        return Response('Could not generate a result, please insure all fields are filled!', status=400)


    result: Result = prediction[0]

    if (result == Result.INVALID):
        return Response('Your result was -1 (invalid). The LeptoClassifier could not construct a result from the data provided. Please make sure that all the data is entered correctly and resubmit. If you are still having trouble please contact us.', status=400)

    temp_link = ''.join(random.choices(string.ascii_letters, k=45))

    dog = db.DogEntry(result, temp_link, request_data);
    
    if (result != -1):
        print("Valid");
        db.put_dog_entry(con, cur, dog);

    #response = make_response(gen_pdf(df, result))
    #response.headers.set("Content-Type", "application/pdf")
    gen_pdf(df,result, temp_link);
    return redirect('/result?temp_link=' + temp_link);

@app.route("/resultcontent/<file_name>")
def get_pdf(file_name):
    return send_file(f"./generated_pdfs/{file_name}",mimetype='application/pdf')

@app.route("/submit_contact", methods=['POST'])
def submit_contact():
    request_data = request.form;
    print(request_data);

    if request_data["name"] == None or request_data["email"] == None or request_data["issue"] == None:
        return 'Missing form value'

    db.put_contact_message(con, cur, request_data["name"], request_data["email"], request_data["issue"])

    return 'Thank you for your message, we will try to get back to you as soon as we can! <strong>You will be redirected to the home page in 5 seconds.</strong><script>setTimeout(callBack_func, 5000); function callBack_func() { document.location.href = "/"; }</script>';
