import os
from flask import Flask, request, render_template, send_file
import PyPDF2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def merge_pdfs(pdf_files, output_path, password=None):
    merger = PyPDF2.PdfMerger()
    
    for filename in pdf_files:
        try:
            with open(filename, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                merger.append(pdf_reader)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except PyPDF2.errors.PdfReadError:
            print(f"Error reading {filename}. It may not be a valid PDF.")

    with open(output_path, 'wb') as merged_file:
        merger.write(merged_file)
    
    if password:
        with open(output_path, 'rb') as merged_file:
            reader = PyPDF2.PdfReader(merged_file)
            writer = PyPDF2.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.encrypt(password)
            with open(output_path, 'wb') as encrypted_file:
                writer.write(encrypted_file)

    merger.close()
    print(f"PDFs merged successfully into {output_path}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    pdf_files = request.files.getlist('pdf_files')
    password = request.form.get('password')
    
    pdf_paths = []
    for pdf in pdf_files:
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf.filename)
        pdf.save(pdf_path)
        pdf_paths.append(pdf_path)
    
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')
    
    merge_pdfs(
        pdf_paths,
        output_path,
        password=password if password else None
    )
    
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
