#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Renders index.html """
    return render_template('content/home.html')

@app.route('/about', strict_slashes=False)
def about():
    """ Renders index.html """
    return render_template('content/about.html')

@app.route('/service', strict_slashes=False)
def service():
    """ Renders index.html """
    return render_template('content/service.html')

@app.route('/service/generated', strict_slashes=False)
def AI_service():
    """ Renders index.html """
    return render_template('content/AI_Genrated.html')

@app.route('/register', strict_slashes=False)
def register():
    """ Renders index.html """
    return render_template('content/register.html')

@app.route('/login', strict_slashes=False)
def login():
    """ Renders index.html """
    return render_template('content/login.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
