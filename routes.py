from pixellock import app
from flask import render_template
import os

UPLOAD_FOLDER = 'static/processed'
ALLOWED_EXTENSIONS = {'png'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Rota que exibe a home page
@app.route('/')
def home():
    return render_template('home.html')
