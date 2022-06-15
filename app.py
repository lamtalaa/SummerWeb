from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def get_index():
    return "<p>This is my awesome new website!</p>"

@app.route("/hello")
def get_hello():
    return render_template('hello.html', name = "Yassine")

@app.route("/santa")
def get_santa():
    return render_template('hello.html', name = "Santa")