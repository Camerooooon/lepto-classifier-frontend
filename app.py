from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route("/")
def index():
    # Return the index.html file
    return render_template('index.html')

@app.route("/submit_data", methods=['POST'])
def submit_data():
    request_data = request.form
    print(request_data);
    return Response("Ok!", status=200)
