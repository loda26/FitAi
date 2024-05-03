#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, request , render_template, redirect, url_for
import requests
from models.user import Users, Session

app = Flask(__name__)
session = Session()

@app.route('/', strict_slashes=False)
def home():
    """ Renders index.html """
    return render_template('content/home.html')

@app.route('/about', strict_slashes=False)
def about():
    """ Renders index.html """
    return render_template('content/about.html')

@app.route('/service', methods=['GET', 'POST'], strict_slashes=False)
def service():
    """ Renders index.html """
    return render_template('content/service.html')

@app.route('/service/generated', methods=['GET', 'POST'], strict_slashes=False)
def AI_service():
    """ Renders index.html """
    url = "https://api.openai.com/v1/chat/completions"
    if request.method == 'POST':
        prompt = request.form['prompt']
# prompt = "translate to me to french: 'Hello, how are you?'"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_api_key"
    }
    data = {
        "messages": [
            {
                "role": "system",
                "content": "User: " + prompt
            }
        ],

        "max_tokens": 1000,
        "model": "gpt-3.5-turbo"
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    data = response_data["choices"][0]["message"]["content"]
    return render_template('content/AI_Genrated.html',data=data)

@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conf_password = request.form['conf_password']
        age = request.form['age']
        gender = request.form['gender']

        if password != conf_password:
            return "Password and confirmation password do not match. Please try again."

        new_user = Users(name=name, email=email, password=password, conf_password=conf_password, age=age, gender=gender)
        session.add(new_user)
        session.commit()

        return render_template('content/login.html')
    
    if request.method == 'GET':
        return render_template('content/register.html')

@app.route('/login', strict_slashes=False)
def login():
    """ Renders index.html """
    return render_template('content/login.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
