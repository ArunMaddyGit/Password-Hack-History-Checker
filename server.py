from flask import Flask, render_template, url_for, request, redirect
import requests
import checkmypass
app = Flask(__name__)
# print(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<string:page_name>")
def display_page(page_name):
    return render_template(page_name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data=request.form['text']
        # print(data)
        msg=checkmypass.main(data)
    # return f"submitted {data}  {msg}"
    return render_template("index.html",message=msg)
    # return 
