from flask import Flask
lexus = Flask(__name__)

@lexus.route('/')
def home():
    return('hello')