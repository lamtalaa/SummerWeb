from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_index():
    return "<p>This is my awesome new website!</p>"

@app.route("/hello")
def get_hello():
    return "<p>Hello There!</p>"