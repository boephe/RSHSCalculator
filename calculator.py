# --------------------------------------------------------------------------
# Simple Python Calculator Web App Using Flask
# --------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------
from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template

# --------------------------------------------------------------------------
# Login Functions
# --------------------------------------------------------------------------
def do_login():
    return "Yay"

def show_login():
    return "login please"

# --------------------------------------------------------------------------
# Calculator Functions
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# Flask Page Setup
# --------------------------------------------------------------------------
app = Flask(__name__)

@app.route("/")
def index():
    nav_item = []
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    else:
        return show_login()