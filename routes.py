import os
from io import BytesIO

from pixellock import app
from flask import flash, redirect, render_template, request, send_from_directory, send_file
from esteganogram import Esteganograma

UPLOAD_FOLDER = 'static/processed'
ALLOWED_EXTENSIONS = {'png'}
Esteganograma = Esteganograma()

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Rota que exibe a home page
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/processar/criptografar', methods=['POST'])
def processCript():
    if request.method == 'POST':

        if 'imagem' not in request.files:
            flash("Nenhum arquivo enviado", 400)
            return redirect('/upload')
        file = request.files['imagem']
        if file.filename == '':
            flash("Nenhum arquivo selecionado", 400)
            return redirect('/upload')
        
        if file and allowed_file(file.filename):
            file.stream.seek(0)
            encryptedFile = Esteganograma.hide_text_in_image(file, request.form['mensagem'])
            img_io = BytesIO()
            encryptedFile.save(img_io, format='PNG')
            img_io.seek(0)
            base_filename = os.path.splitext(file.filename)[0]
            filename = base_filename + '_encrypted.png'
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=filename)
        
        else:
            flash("Formato de arquivo não permitido. Use PNG.", 400)
            return render_template('upload.html', error="Formato de arquivo não permitido. Use PNG.")
    else:
        flash("Método não permitido", 405)
        return render_template('upload.html', error="Formato de arquivo não permitido. Use PNG.")
    
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


@app.route('/revelar', methods=['GET', 'POST'])
def reveal():
    return render_template('reveal.html')

@app.route('/processar/descriptografar', methods=['POST'])
def processDecript():
    if request.method == 'POST':
        if 'imagem' not in request.files:
            flash("Nenhum arquivo enviado", 400)
            return redirect('/revelar')
        
        file = request.files['imagem']
        if file.filename == '':
            flash("Nenhum arquivo selecionado", 400)
            return redirect('/revelar')
        
        try:
            file.stream.seek(0)
            mensagem = Esteganograma.extract_text_from_image(file)

            if "Erro" in mensagem:
                return render_template('reveal.html', error=mensagem)
            
            return render_template('reveal.html', mensagem=mensagem)
        except Exception as e:
            flash(f"Erro ao processar imagem: {str(e)}", 500)
            return redirect('/revelar')
    else:
        flash("Método não permitido", 405)
        return redirect('/revelar')