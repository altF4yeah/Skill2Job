import os
import PyPDF2
import docx

def extract_text(filepath):
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    
    if ext == '.pdf':
        return extract_text_from_pdf(filepath)
    elif ext in ['.doc', '.docx']:
        return extract_text_from_docx(filepath)
    else:
        return None

def extract_text_from_pdf(filepath):
    text = ""
    try:
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"PDF Extraction Error: {e}")
    return text

def extract_text_from_docx(filepath):
    text = ""
    try:
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"DOCX Extraction Error: {e}")
    return text