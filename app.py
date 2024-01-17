from flask import Flask, request, send_file, render_template
from pdf2docx import Converter
from config import Config
import os

app = Flask(__name__)
UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
CONVERTED_FOLDER = app.config['CONVERTED_FOLDER']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# not needed with s3
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

if not os.path.exists(CONVERTED_FOLDER):
    os.mkdir(CONVERTED_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return 'No file in the request...'
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected for uploading'
    
    if file and not file.filename.endswith('.pdf'):
        return 'Invalid file format. We only currently support PDF files.'
    
    else:
        pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
        docx_path = os.path.join(CONVERTED_FOLDER, os.path.splitext(file.filename)[0] + '.docx')
        file.save(pdf_path)

        converter = Converter(pdf_path)
        converter.convert(docx_path)
        converter.close()

        return send_file(docx_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
