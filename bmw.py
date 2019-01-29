from flask import flask

lexus = Flask(__name__)

@app.route('/')
def home():
    return('hello')