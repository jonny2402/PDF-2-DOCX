# PDF to DOCX Converter

This is a simple web application that allows users to convert PDF files to DOCX format.

## Features

- Upload a PDF file
- Convert the uploaded PDF to DOCX
- Download the converted DOCX file

## Usage

1. Start the Flask server: python app.py

2. Open a web browser and navigate to `http://localhost:5000`.

3. Upload a PDF file and click on the 'Convert' button.

4. After the conversion is complete, the DOCX file will be automatically downloaded.

## Dependencies

- Flask
- pdf2docx

## TODO

- Update user on progress of conversion using eg. progress bar
- Styling
- Store files in S3 + host on EC2?