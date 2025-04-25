# PDFUnify: Merge Multiple PDFs into One

**PDFUnify** is a simple and secure Flask-based web application that lets users upload multiple PDF files and merge them into a single document. Users can optionally **encrypt** the output PDF with a password.

---

## 🔍 Problem Statement

Merging multiple PDF files manually is time-consuming, and many free tools come with file size limits or ads. PDFUnify provides an ad-free, offline-capable web interface to combine PDFs instantly and securely, with optional encryption for added privacy.

---

## 📁 Project Structure

```
PDFUnify-Flask-app/
├── app.py                 # Flask backend for uploading, merging, and encrypting PDFs
├── templates/
│   └── index.html         # Frontend UI for file upload and password input
├── uploads/               # Temporary storage for uploaded and merged files
└── requirements.txt       # Required Python packages
```

---

## ⚙️ Features

- Upload **multiple PDF files**
- Merge them into a **single PDF**
- Optional **password encryption** for security
- Download the final PDF with a single click
- Error handling for:
  - Invalid or corrupt PDFs
  - Missing files

---

## 🎨 Web App Flow

1. User selects and uploads multiple PDF files
2. Optionally enters a password for encryption
3. App merges the files into `merged.pdf`
4. Encrypted if password is provided
5. Final PDF is returned as a downloadable file

---

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/ankitakedia2003/PDFUnify-Flask-app.git
cd PDFUnify-Flask-app
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Create Upload Folder (if not exists)

```bash
mkdir uploads
```

### Step 4: Run the App

```bash
python app.py
```

Access the app at `http://localhost:5000`

---

## 🔐 Optional Encryption

If a password is entered in the form, the merged PDF will be encrypted using that password. This ensures secure access to the document.

---

## ✨ Built With

- [Flask](https://flask.palletsprojects.com/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)

---

## 🌐 Live Demo

Vercel App: https://pdf-unify-flask-app.vercel.app/
