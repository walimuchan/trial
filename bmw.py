from flask import Flask
lexus = Flask(__name__)

@lexus.route('/')
def home():
    return('hello')



if __name__ == '__main__':
    lexus.run(debug=True)