from flask import Flask

app = Flask(__name__)

from routes import *
import os

app.secret_key = os.urandom(24)

if __name__ == '__main__':   
    app.run(debug=True)