from flask import flask

lexus = Flask(__name__)

@lexus.route('/')
def home():
    return('hello')