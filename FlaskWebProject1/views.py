"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hci')
def hci():
    return render_template('HCI.html')

@app.route('/hw3')
def hw3():
    return render_template('hw3.html')
