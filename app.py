from flask import Flask, render_template, request, send_file, redirect, url_for
from result import Result, from_prediction
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

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def main():
    # Return the intro.html file
    return render_template('main.html')

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


    print(prediction[0])
    result: Result = from_prediction(prediction[0])

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
