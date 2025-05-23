from flask import Flask
hello_app = Flask(__name__)
@hello_app.route('/')
def hello():
    return 'Hello, World!'