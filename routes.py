from pixellock import app
from flask import render_template

@app.route('/')
def home():
    return render_template('upload.html')
