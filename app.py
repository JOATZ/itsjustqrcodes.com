from flask import Flask
qrcodes_app = Flask(__name__)

@qrcodes_app.route('/')
def hello():
    return 'Hello World!'