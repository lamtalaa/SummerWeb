from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, make_response
from flask import session

app = Flask(__name__)
app.secret_key = "qwertyuioplkjhgfdsazxcvbnm"

username = None

@app.route("/")
@app.route("/home")
def get_index():
    if "username" in session:
        username = session['username']
    else:
        return redirect (url_for('get_login'))
    return render_template('home.html', name = username)

@app.route("/other")
def get_other():
    if "username" in session:
        username = session['username']
    else:
        return redirect (url_for('get_login'))
    return render_template('other.html', name = username)

@app.route("/login", methods=['GET'])
def get_login():
    username = request.cookies.get("username", None)
    if username != None:
        return redirect (url_for('get_index'))
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def post_login():
    username = request.form.get("username", None)
    if username != None:
        session['username'] = username
        return redirect (url_for('get_index'))
    else:
        return redirect (url_for('get_login'))

@app.route("/logout", methods=['GET'])
def get_logout():
    session.pop('username', None)
    return redirect (url_for('get_login'))